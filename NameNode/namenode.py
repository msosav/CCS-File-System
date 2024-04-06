"""
NameNode
"""

import grpc
from concurrent import futures
import namenode_pb2
import namenode_pb2_grpc

class NameNodeServiceServicer(namenode_pb2_grpc.NameNodeServiceServicer):
    def ListFiles(self, request, context):
        ls_files = files.keys()
        return namenode_pb2.ListFilesResponse(files=ls_files)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    namenode_pb2_grpc.add_NameNodeServiceServicer_to_server(NameNodeServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}


def distribute_file(file_name, num_partitions, size):
    """
    Distribuye un archivo en los datanodes
    param file_name: El nombre del archivo
    param num_partitions: La lista de partes del archivo
    return: El diccionario de datanodes
    """
    datanodes[file_name] = {}
    datanode_index = 0
    for i in range(num_partitions):
        if datanode_index >= len(active_datanodes):
            datanode_index = 0
        datanodes[file_name][partition_name(
            i)] = [active_datanodes[datanode_index]]
        datanode_index += 1
    files[file_name] = size
    return datanodes[file_name]


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


def locate_file(file_name):
    """
    Localiza un archivo
    param file_name: El nombre del archivo
    return: La lista de ubicaciones del archivo
    """
    if file_name not in datanodes:
        return []
    return datanodes[file_name]

def file_system(option):
    """
    Muestra el sistema de archivos
    param option: La opción a mostrar
    return: None
    """
    if option == "ls":
        return files
    else:
        return "Invalid option"


if __name__ == "__main__":
    active_datanodes = ["Datanode1", "Datanode2"]
    files = {"file1": 1000, "file2": 2000}
    serve()

