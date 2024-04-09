from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
import os
import time
from threading import Thread


def get_replication_url(partition_name, file_name):
    """
    Realiza una solicitud a la URL
    param partition_name: El nombre de la partición
    return: None
    """
    channel = grpc.insecure_channel("localhost:8080")
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.ReplicationUrl(
        Service_pb2.ReplicationUrlRequest(
            partition_name=partition_name, file_name=file_name
        )
    )
    return response.url


class DataNodeServicer(Service_pb2_grpc.DataNodeServicer):
    def SendPartition(self, request, context):
        """
        Envía una partición
        param request: La partición a enviar
        return: None
        """
        file_name = request.file_name
        partition_name = request.partition_name
        os.makedirs(file_name, exist_ok=True)
        storage_path = f"{file_name}/{partition_name}"
        with open(storage_path, "wb") as f:
            f.write(request.partition_data)
        channel = grpc.insecure_channel("localhost:8080")
        stub = Service_pb2_grpc.NameNodeStub(channel)
        reponse = stub.SaveNodeFile(
            Service_pb2.SaveNodeFileRequest(
                file_name=file_name,
                url="localhost:50051",
                partition_name=partition_name,
            )
        )
        if request.current_replication < 3:
            request.current_replication += 1
            url = get_replication_url(partition_name, file_name)
            if url == "":
                return Service_pb2.SendPartitionResponse(status_code=200)
            with grpc.insecure_channel(url) as channel:
                stub = Service_pb2_grpc.DataNodeStub(channel)
                stub.SendPartition(request)
        return Service_pb2.SendPartitionResponse(status_code=200)

    def DownloadPartition(self, request, context):
        file_name = request.file_name
        partition_name = request.partition_name
        storage_path = f"{file_name}/{partition_name}"
        with open(storage_path, "rb") as partition:
            data = partition.read()
        return Service_pb2.DownloadPartitionResponse(partition_data=data)


    def Replicate(self, request, context):
        file_name = request.file_name
        partition_name = request.partition_name
        url = request.url
        file_path = os.path.join(file_name, partition_name)
        if not os.path.exists(file_path):
            return Service_pb2.ReplicateResponse(status_code=404)
        with open(file_path, "rb") as file:
            partition_data = file.read()
        with grpc.insecure_channel(url) as channel:
            stub = Service_pb2_grpc.DataNodeStub(channel)
            stub.SendPartition(
                Service_pb2.SendPartitionRequest(
                    file_name=file_name,
                    partition_name=partition_name,
                    partition_data=partition_data,
                    current_replication=3,
                )
            )
        return Service_pb2.ReplicateResponse(status_code=200)


def send_heartbeats():
    """
    Envía latidos
    return: None
    """
    while True:
        timestamp = int(time.time())
        try:
            channel = grpc.insecure_channel("localhost:8080")
            stub = Service_pb2_grpc.NameNodeStub(channel)
            stub.HeartBeat(
                Service_pb2.HeartBeatRequest(url="localhost:50051", timestamp=timestamp)
            )
        except Exception as e:
            print(e)
        time.sleep(10)


def save_node_file(file_name):
    """
    Notifica al name node que se guardó un archivo
    param file_name: El nombre del archivo
    return: None
    """
    channel = grpc.insecure_channel("localhost:8080")
    stub = Service_pb2_grpc.NameNodeStub(channel)
    stub.SaveNodeFile(
        Service_pb2.SaveNodeFileRequest(file_name=file_name, url="localhost:50051")
    )


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_DataNodeServicer_to_server(DataNodeServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    send_heartbeats_thread = Thread(target=send_heartbeats)
    send_heartbeats_thread.daemon = True
    send_heartbeats_thread.start()
    server.wait_for_termination()
