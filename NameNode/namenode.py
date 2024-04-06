"""
NameNode
"""

import ccs_pb2
import ccs_pb2_grpc
from concurrent import futures
import grpc
import random

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}

active = []
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

class FileTransferServicer(ccs_pb2_grpc.FileTransferService):
    def GetUrl(self, request, context):
        print(f"Received request for URL of file '{request.file_name}'")
        if (not active):
            return ccs_pb2.urlResponse(url="")
        if request.file_name not in files:
            print("what")
            url = random.choice(active)
            print("hola" + url)
            return ccs_pb2.urlResponse(url= url)
        else:
            active_urls = [x for x in active if x not in files[request.file_name]]
            if not active_urls:
                return ccs_pb2.urlResponse(url="")
            url = random.choice(active_urls)
            return ccs_pb2.urlResponse(url=url)


if __name__ == "__main__":
    active = ['localhost:50051']
    files = {'file1': ['localhost:50051'], 'file2': ['localhost:50052']}
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ccs_pb2_grpc.add_FileTransferServiceServicer_to_server(FileTransferServicer(), server)
    server.add_insecure_port("localhost:50050")
    server.start()
    server.wait_for_termination()
