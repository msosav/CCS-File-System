"""
NameNode
"""

from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
import random
from threading import Thread
import time

# Diccionario que almacena los datanodes y los archivos que contienen
datanodes = {}
active_datanodes = []
files = {}
heartbeats = {}


def distribute_file(file_name, num_partitions, size, response, start_from=0):
    """
    Distribuye un archivo en los datanodes
    param file_name: El nombre del archivo
    param num_partitions: La lista de partes del archivo
    return: El diccionario de datanodes
    """
    datanode_index = 0
    for i in range(start_from, num_partitions):
        if datanode_index >= len(active_datanodes):
            datanode_index = 0
        response.partitions[partition_name(i)] = active_datanodes[datanode_index]
        if file_name not in datanodes:
            datanodes[file_name] = {}
        datanodes[file_name][partition_name(i)] = [active_datanodes[datanode_index]]
        datanode_index += 1
    print(datanodes)
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


class NameNodeServicer(Service_pb2_grpc.NameNodeServicer):
    def Create(self, request, context):
        """
        Crea un archivo
        param request: El archivo a crear
        return: El diccionario de datanodes
        """
        file_name = request.file_name
        num_partitions = request.num_partitions
        size = request.size
        last_partition_urls = []
        response = Service_pb2.CreateResponse()
        if file_name in files:
            last_num_partitions = len(datanodes[file_name].keys())
            last_partition_urls = datanodes[file_name][partition_name(last_num_partitions - 1)]
            distribute_file(file_name, num_partitions, size, response, last_num_partitions - 1)
            response.last_partition_urls.extend(last_partition_urls)
        else:
            distribute_file(file_name, num_partitions, size, response)
        response.status_code = 200
        return response

    def ListFiles(self, request, context):
        """
        Lista los archivos
        return: None
        """
        response = Service_pb2.ListFilesResponse()
        for key, value in files.items():
            response.files[key] = value
        return response

    def ReplicationUrl(self, request, context):
        """
        Realiza una solicitud a la URL
        param request: La solicitud
        return: La URL
        """
        if not active_datanodes:
            return Service_pb2.ReplicationUrlResponse(url="")
        partitions_of_file = datanodes[request.file_name]
        if request.partition_name not in partitions_of_file.keys():
            url = random.choice(active_datanodes)
            return Service_pb2.ReplicationUrlResponse(url=url)
        else:
            active_urls = [
                x for x in active_datanodes if x not in partitions_of_file]
            if not active_urls:
                return Service_pb2.ReplicationUrlResponse(url="")
            url = random.choice(active_urls)
            return Service_pb2.ReplicationUrlResponse(url=url)

    def HeartBeat(self, request, context):
        """
        Realiza un latido
        param request: El latido
        return: None
        """
        if request.url not in active_datanodes:
            active_datanodes.append(request.url)
        heartbeats[request.url] = request.timestamp
        return Service_pb2.HeartBeatResponse(message="OK")

    def SaveNodeFile(self, request, context):
        """
        Guardar que un data node tiene un archivo
        param request: El archivo a guardar
        return: None
        """
        file_name = request.file_name
        partition_name = request.partition_name
        if file_name not in datanodes:
            datanodes[file_name] = {}
        if partition_name not in datanodes[file_name]:
            datanodes[file_name][partition_name] = []
        if request.url in datanodes[file_name][partition_name]:
            return Service_pb2.SaveNodeFileResponse(message="OK")
        datanodes[file_name][partition_name].append(request.url)
        return Service_pb2.SaveNodeFileResponse(message="OK")

    def Download(self, request, context):
        """
        Descarga un archivo
        param request: El archivo a descargar
        return: El archivo
        """
        file_name = request.file_name
        response = Service_pb2.DownloadResponse()
        datanodes_of_file = datanodes[file_name]
        for partition_name, urls in datanodes_of_file.items():
            data_node_info = Service_pb2.DataNodeInfo()
            data_node_info.url.extend(urls)
            response.partitions[partition_name].CopyFrom(data_node_info)
        return response
    
    def DeleteNodeFile(self, request, context):
        """
        Elimina un archivo
        param request: El archivo a eliminar
        return: None
        """
        file_name = request.file_name
        partition_name = request.partition_name
        if file_name not in datanodes:
            return Service_pb2.DeleteNodeFileResponse(message="OK")
        if partition_name not in datanodes[file_name]:
            return Service_pb2.DeleteNodeFileResponse(message="OK")
        datanodes[file_name][partition_name].remove(request.url)
        return Service_pb2.DeleteNodeFileResponse(message="OK")
        
    
def monitor_heartbeats_and_replication():
    while True:
        time.sleep(15)
        print(datanodes)
        current_time = int(time.time())
        for url, timestamp in list(heartbeats.items()):
            if current_time - timestamp > 15:
                print(f"DataNode {url} is inactive, removing from active list")
                active_datanodes.remove(url)
                del heartbeats[url]
                if not datanodes:
                    continue
                for file_name, partitions in datanodes.items():
                    for partition_name, urls in partitions.items():
                        if url in urls:
                            datanodes[file_name][partition_name].remove(url)
                            print(
                                f"DataNode {url} removed from partition {
                                    partition_name} of file {file_name}"
                            )
        if not datanodes:
            continue
        for file_name, partitions in datanodes.items():
            if not file_name or not partitions:
                continue
            for partition_name, urls in partitions.items():
                if not partition_name or not urls:
                    continue
                if len(urls) < 3:
                    missing_urls = [url for url in active_datanodes if url not in urls]
                    if missing_urls:
                        urlWithFile = random.choice(urls)
                        url = random.choice(missing_urls)
                        with grpc.insecure_channel(urlWithFile) as channel:
                            stub = Service_pb2_grpc.DataNodeStub(channel)
                            stub.Replicate(
                                Service_pb2.ReplicateRequest(
                                    file_name=file_name,
                                    partition_name=partition_name,
                                    url=url,
                                )
                            )
                


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_NameNodeServicer_to_server(NameNodeServicer(), server)
    server.add_insecure_port("localhost:8080")
    server.start()
    print("NameNode running at port 8080.")
    monitor_heartbeats_thread = Thread(target=monitor_heartbeats_and_replication)
    monitor_heartbeats_thread.daemon = True
    monitor_heartbeats_thread.start()
    server.wait_for_termination()
