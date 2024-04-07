from concurrent import futures
import grpc
import Service_pb2
import Service_pb2_grpc
import os
import time
from threading import Thread


def get_extension(file_name):
    """
    Obtiene la extensión de un archivo
    param file_name: El nombre del archivo
    return: La extensión del archivo
    """
    return file_name.split(".")


def get_replication_url(partition_name, file_name):
    """
    Realiza una solicitud a la URL
    param partition_name: El nombre de la partición
    return: None
    """
    channel = grpc.insecure_channel('localhost:8080')
    stub = Service_pb2_grpc.NameNodeStub(channel)
    response = stub.ReplicationUrl(
        Service_pb2.ReplicationUrlRequest(partition_name=partition_name, file_name=file_name))
    return response.url


class DataNodeServicer(Service_pb2_grpc.DataNodeServicer):
    def SendPartition(self, request, context):
        file_name = request.file_name
        partition_name = request.partition_name
        os.makedirs(file_name, exist_ok=True)
        storage_path = f"{file_name}/{partition_name}"
        with open(storage_path, "wb") as f:
            f.write(request.partition_data)


def send_heartbeats():
    while True:
        timestamp = int(time.time())
        try:
            channel = grpc.insecure_channel("localhost:50050")
            stub = ccs_pb2_grpc.FileTransferServiceStub(channel)
            stub.Heart(ccs_pb2.HeartRequest(
                url="localhost:50051", timestamp=timestamp))
        except Exception as e:
            print(e)
        time.sleep(10)


# Sleep for 10 seconds before sending the next heartbeat


def save_node_file(file_name):
    channel = grpc.insecure_channel("localhost:50050")
    stub = ccs_pb2_grpc.FileTransferServiceStub(channel)
    stub.SaveNodeFile(
        ccs_pb2.SaveNodeFileRequest(file_name=file_name, url="localhost:50051")
    )


class FileTransferServicer(ccs_pb2_grpc.FileTransferService):
    def TransferFile(self, request, context):
        print("llegueeeeeeeeee")
        name = get_extension(request.file_name)[0]
        extension = get_extension(request.file_name)[1]
        with open(f"{name}${request.current_replication}.{extension}", "wb") as f:
            f.write(request.file_data)
        save_node_file(request.file_name)
        if request.current_replication < 3:
            print(
                f"Replicating '{request.current_replication}' of file '{
                    request.file_name}"
            )
            request.current_replication += 1
            url = get_replication_url(partition_name, file_name)
            if url == "":
                return Service_pb2.SendPartitionResponse(status_code=200)
            with grpc.insecure_channel(url) as channel:
                stub = Service_pb2_grpc.DataNodeStub(channel)
                stub.SendPartition(request)
        return Service_pb2.SendPartitionResponse(status_code=200)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_DataNodeServicer_to_server(
        DataNodeServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    send_heartbeats_thread = Thread(target=send_heartbeats)
    send_heartbeats_thread.daemon = True
    send_heartbeats_thread.start()
    server.wait_for_termination()
