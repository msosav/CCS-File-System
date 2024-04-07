"""
NameNode
"""
from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc

import ccs_pb2
import ccs_pb2_grpc
import random
from concurrent import futures
import namenode_pb2
import namenode_pb2_grpc
import time
from threading import Thread


class NameNodeServiceServicer(namenode_pb2_grpc.NameNodeServiceServicer):
    def ListFiles(self, request, context):
        ls_files = files.keys()
        return namenode_pb2.ListFilesResponse(files=ls_files)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    namenode_pb2_grpc.add_NameNodeServiceServicer_to_server(
        NameNodeServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}
heartbeats = {}

active_datanodes = []
files = {}


def distribute_file(file_name, num_partitions, size, response):
    """
    Distribuye un archivo en los datanodes
    param file_name: El nombre del archivo
    param num_partitions: La lista de partes del archivo
    return: El diccionario de datanodes
    """
    datanode_index = 0
    for i in range(num_partitions):
        if datanode_index >= len(active_datanodes):
            datanode_index = 0
        response.partitions[partition_name(
            i)] = active_datanodes[datanode_index]
        datanode_index += 1
    files[file_name] = size
    return response


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


def locate_file(file_name):
    """
    Localiza un archivo
    param file_name: El nombre del archivo
    return: La lista de ubicaciones del archivo
    """
    if file_name not in datanodes:
        return []
    return datanodes[file_name]


class NameNodeServicer(Service_pb2_grpc.NameNodeServicer):
    def CreateRequest(self, request, context):
        """
        Crea un archivo
        param request: El archivo a crear
        return: El diccionario de datanodes
        """
        file_name = request.file_name
        num_partitions = request.num_partitions
        size = request.size
        response = Service_pb2.CreateResponse()
        response = distribute_file(file_name, num_partitions, size, response)
        return response


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
    
def monitor_heartbeats():
    while True:
        time.sleep(15)
        current_time = int(time.time())
        for url, beat in list(heartbeats.items()):
            if current_time - int(beat) > 15:
                print(f"DataNode {url} is inactive, removing from active list")
                active_datanodes.remove(url)
                del heartbeats[url]
        


class FileTransferServicer(ccs_pb2_grpc.FileTransferService):
    def GetUrl(self, request, context):
        print(f"Received request for URL of file '{request.file_name}'")
        if not active_datanodes:
            return ccs_pb2.urlResponse(url="")
        if request.file_name not in files:
            url = random.choice(active_datanodes)
            return ccs_pb2.urlResponse(url=url)
        else:
            active_urls = [
                x for x in active_datanodes if x not in files[request.file_name]]
            if not active_urls:
                return ccs_pb2.urlResponse(url="")
            url = random.choice(active_urls)
            return ccs_pb2.urlResponse(url=url)
    def SaveNodeFile(self, request, context):
        print(f"Received request to save file '{request.file_name}'")
        if request.file_name not in files:
            files[request.file_name] = [request.url]
        else:
            files[request.file_name].append(request.url)
        print(files[request.file_name])
        return ccs_pb2.SaveNodeFileResponse(message="File saved.")
    def HeartBeat(self, request, context):
        print(f"Received heartbeat from datanode '{request.url}'")
        heartbeats[request.url] = request.beat
        return ccs_pb2.HeartbeatResponse(message="File saved.")


if __name__ == "__main__":
    active_datanodes = ["localhost:50051"]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ccs_pb2_grpc.add_FileTransferServiceServicer_to_server(FileTransferServicer(), server)
    server.add_insecure_port('localhost:50050')
    server.start()
    print("NameNode running at port 8080.")
    # monitor_heartbeats_thread = Thread(target=monitor_heartbeats)
    # monitor_heartbeats_thread.daemon = True
    # monitor_heartbeats_thread.start()
    server.wait_for_termination()
