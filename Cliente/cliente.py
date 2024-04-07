"""
Cliente
"""

import os
import Service_pb2
import Service_pb2_grpc
import grpc
import shutil


def list_files():
    """
    Lista los archivos
    return: None
    """
    channel = grpc.insecure_channel('localhost:8080')
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.ListFiles(Service_pb2.ListFilesRequest())
    files = response.files
    alphabetically = sorted(files.keys())
    for file in alphabetically:
        print(f"{file} - {files[file]} MB")


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

    with open(file_name, 'r') as file:
        content = file.read()

    num_partitions = (len(content) + partition_size - 1) // partition_size

    for i in range(num_partitions):
        partition_content = content[i *
                                    partition_size: (i + 1) * partition_size]
        output_file = f"{path}/{partition_name(i)}"
        with open(output_file, 'w') as file:
            file.write(partition_content)

    return num_partitions


def partition_name(i):
    """
    Genera el nombre de la partición
    param i: El número de la partición
    return: El nombre de la partición
    """
    length = len(str(i))
    serial = '0' * (4 - length) + str(i)
    name = f"part-{serial}"
    return name


def join_files(file_name, num_partitions=10000):
    """
    Une las particiones de un archivo
    param file_name: El archivo a unir
    param num_partitions: El número máximo de particiones
    return: None
    """
    storage = "Storage"
    path = os.path.join(storage, file_name)

    if not os.path.isdir(path):
        raise FileNotFoundError(f"Directory '{file_name}' not found.")

    output_file = f"output_{file_name}"
    with open(output_file, 'w') as output:
        for i in range(num_partitions):
            partition_file = f"{path}/{partition_name(i)}"
            if not os.path.isfile(partition_file):
                break
            with open(partition_file, 'r') as partition:
                output.write(partition.read())

    print(f"Partitions of file '{file_name}' joined into '{output_file}'.")


def read_file(file):
    """
    Lee un archivo
    param file: El archivo a leer
    return: None
    """
    with open(file, 'rb') as file:
        print(file.read())


def upload_file(file_name, num_partitions, size):
    """
    Sube un archivo
    param file_name: El archivo a subir
    param num_partitions: El número de particiones
    param size: El tamaño del archivo
    return: None
    """
    channel = grpc.insecure_channel('[::]:8080')
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.Create(
        Service_pb2.CreateRequest(file_name=file_name, num_partitions=num_partitions, size=size))
    partitions = response.partitions  # key: partition_name, value: datanode

    for partition_name, datanode in partitions.items():
        partition_path = f"client_temp/{file_name}/{partition_name}"
        with open(partition_path, 'rb') as partition:
            data = partition.read()
            request = Service_pb2.SendPartitionRequest(
                file_name=file_name, partition_name=partition_name, partition_data=data, current_replication=0)
            with grpc.insecure_channel(datanode) as channel:
                stub = Service_pb2_grpc.DataNodeStub(channel)
                response = stub.SendPartition(request)

    shutil.rmtree("client_temp")


def upload_file(file_name):
    url = url_request(file_name)

    if url == "":
        print("No available datanodes.")
        return

    with grpc.insecure_channel(url) as channel:
        stub = ccs_pb2_grpc.FileTransferServiceStub(channel)

        with open(file_name, "rb") as f:
            file_data = f.read()

        response = stub.TransferFile(
            ccs_pb2.TransferRequest(
                file_data=file_data, file_name=file_name, current_replication=1
            )
        )
    print(response.message)


if __name__ == '__main__':
    while True:
        command = input()
        command_args = command.split(" ")
        instruction = command_args[0]
        if instruction == 'exit':
            break
        elif instruction == 'upload':
            file_name = command_args[1]
            num_partitions = partition_file(file_name)
            size = os.path.getsize(file_name)
            upload_file(file_name, num_partitions, size)
        elif instruction == 'ls':
            list_files()
