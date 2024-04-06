"""
Cliente
"""

import os
import grpc
import Service_pb2
import Service_pb2_grpc


def partition_file(input_file):
    """
    Divide el archivo en partes de 1000 bytes
    param input_file: El archivo a dividir
    return: El número de particiones
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found.")

    partition_size = 1000
    storage = "Storage"
    path = os.path.join(storage, input_file)
    os.makedirs(path, exist_ok=True)

    with open(input_file, 'r') as file:
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


def join_files(input_file, num_partitions=10000):
    """
    Une las particiones de un archivo
    param input_file: El archivo a unir
    param num_partitions: El número máximo de particiones
    return: None
    """
    storage = "Storage"
    path = os.path.join(storage, input_file)

    if not os.path.isdir(path):
        raise FileNotFoundError(f"Directory '{input_file}' not found.")

    output_file = f"output_{input_file}"
    with open(output_file, 'w') as output:
        for i in range(num_partitions):
            partition_file = f"{path}/{partition_name(i)}"
            if not os.path.isfile(partition_file):
                break
            with open(partition_file, 'r') as partition:
                output.write(partition.read())

    print(f"Partitions of file '{input_file}' joined into '{output_file}'.")


if __name__ == '__main__':
    channel = grpc.insecure_channel('[::]:8080')
    stub = Service_pb2_grpc.NameNodeStub(channel)
    while True:
        command = input()
        command_args = command.split(" ")
        instruction = command_args[0]
        if instruction == 'exit':
            break
        elif instruction == 'create':
            file = command_args[1]
            num_partitions = partition_file(file)
            size = os.path.getsize(file)
            response = stub.CreateRequest(
                Service_pb2.Create(file_name=file, num_partitions=num_partitions, size=size))
            partitions = response.partitions  # key: partition_name, value: datanode
        elif instruction == 'read':
            file = command_args[1]
            print(f"Reading file '{file}'")
            join_files(file)
