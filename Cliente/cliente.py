"""
Cliente
"""

import os
import Service_pb2
import Service_pb2_grpc
import grpc
import shutil

import dotenv

dotenv.load_dotenv()

SERVER_URL = os.getenv("SERVER_URL")


def list_files():
    """
    Lista los archivos
    return: None
    """
    channel = grpc.insecure_channel(f"{SERVER_URL}:8080")
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.ListFiles(Service_pb2.ListFilesRequest())
    files = response.files
    alphabetically = sorted(files.keys())
    for file in alphabetically:
        print(f"{file} - {files[file]} KB")


def partition_file(file_name):
    """
    Divide el archivo en partes de 1000 bytes
    param file_name: El archivo a dividir
    return: El número de particiones
    """
    if not os.path.isfile(file_name):
        raise FileNotFoundError(f"File '{file_name}' not found.")

    partition_size = 1000
    temp = "client_temp"
    path = os.path.join(temp, file_name)
    os.makedirs(path, exist_ok=True)

    with open(file_name, "r") as file:
        content = file.read()

    num_partitions = (len(content) + partition_size - 1) // partition_size

    for i in range(num_partitions):
        partition_content = content[i *
                                    partition_size: (i + 1) * partition_size]
        output_file = f"{path}/{partition_name(i)}"
        with open(output_file, "w") as file:
            file.write(partition_content)

    return num_partitions


def partition_name(i):
    """
    Genera el nombre de la partición
    param i: El número de la partición
    return: El nombre de la partición
    """
    length = len(str(i))
    serial = "0" * (4 - length) + str(i)
    name = f"part-{serial}"
    return name


def join_files(file_name, path, num_partitions=10000):
    """
    Une las particiones de un archivo
    param file_name: El archivo a unir
    param num_partitions: El número máximo de particiones
    return: None
    """
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Directory '{file_name}' not found.")
    os.makedirs("Storage", exist_ok=True)
    output_file = f"Storage/{file_name}"
    with open(output_file, "w") as output:
        for i in range(num_partitions):
            partition_file = f"{path}/{partition_name(i)}"
            if not os.path.isfile(partition_file):
                break
            with open(partition_file, "r") as partition:
                output.write(partition.read())


def upload_file(file_name, num_partitions, size):
    """
    Sube un archivo
    param file_name: El archivo a subir
    param num_partitions: El número de particiones
    param size: El tamaño del archivo
    return: None
    """
    channel = grpc.insecure_channel(f"{SERVER_URL}:8080")
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.Create(
        Service_pb2.CreateRequest(
            file_name=file_name, num_partitions=num_partitions, size=size
        )
    )
    last_partition_urls = response.last_partition_urls
    partitions = response.partitions  # key: partition_name, value: datanode
    if not partitions.get("part-0000"):
        first_key = sorted(partitions.keys())[0]
        del partitions[first_key]
        for i in range(len(last_partition_urls)):
            partition_path = f"client_temp/{file_name}/{first_key}"
            with open(partition_path, "rb") as partition:
                data = partition.read()
                request = Service_pb2.SendPartitionRequest(
                    file_name=file_name,
                    partition_name=first_key,
                    partition_data=data,
                    current_replication=3,
                )
                with grpc.insecure_channel(last_partition_urls[i]) as channel:
                    stub = Service_pb2_grpc.DataNodeStub(channel)
                    response = stub.SendPartition(request)
    for partition_name, datanode in partitions.items():
        partition_path = f"client_temp/{file_name}/{partition_name}"
        with open(partition_path, "rb") as partition:
            data = partition.read()
            request = Service_pb2.SendPartitionRequest(
                file_name=file_name,
                partition_name=partition_name,
                partition_data=data,
                current_replication=1,
            )
            with grpc.insecure_channel(datanode) as channel:
                stub = Service_pb2_grpc.DataNodeStub(channel)
                response = stub.SendPartition(request)
    shutil.rmtree("client_temp")


def download_file(file_name):
    channel = grpc.insecure_channel(f"{SERVER_URL}:8080")
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.Download(Service_pb2.DownloadRequest(file_name=file_name))
    partitions = response.partitions
    file_temp_path = f"client_temp/{file_name}"
    os.makedirs(file_temp_path, exist_ok=True)
    for partition, datanodes in partitions.items():
        partition_temp_path = f"client_temp/{file_name}/{partition}"
        with grpc.insecure_channel(datanodes.url[0]) as channel:
            stub = Service_pb2_grpc.DataNodeStub(channel)
            request = Service_pb2.DownloadPartitionRequest(
                partition_name=partition, file_name=file_name
            )
            response = stub.DownloadPartition(request)
        with open(partition_temp_path, "wb") as file:
            file.write(response.partition_data)
    join_files(file_name, file_temp_path)
    shutil.rmtree("client_temp")


if __name__ == "__main__":
    while True:
        command = input()
        command_args = command.split(" ")
        instruction = command_args[0]
        if instruction == "exit":
            break
        elif instruction == "upload":
            file_name = command_args[1]
            num_partitions = partition_file(file_name)
            size = os.path.getsize(file_name)
            upload_file(file_name, num_partitions, size)
            print(f"File {file_name} uploaded successfully")
        elif instruction == "ls":
            list_files()
        elif instruction == "download":
            file_name = command_args[1]
            download_file(file_name)
            print(f"File {file_name} downloaded to Storage folder")
