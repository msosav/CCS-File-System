import ccs_pb2
import ccs_pb2_grpc
from concurrent import futures
import grpc
import time
from threading import Thread


def get_extension(file_name):
    """
    Obtiene la extensión de un archivo
    param file_name: El nombre del archivo
    return: La extensión del archivo
    """
    return file_name.split(".")


def url_request(file_name):
    """
    Realiza una solicitud a la URL
    param file_name: El nombre del archivo
    return: None
    """
    channel = grpc.insecure_channel("localhost:50050")
    stub = ccs_pb2_grpc.FileTransferServiceStub(channel)
    response = stub.GetUrl(ccs_pb2.urlRequest(file_name=file_name))
    return response.url


def send_heartbeats():

    channel = grpc.insecure_channel("localhost:50050")
    stub = ccs_pb2_grpc.FileTransferServiceStub(channel)
    stub.Heartbeat(ccs_pb2.HeartbeatRequest(url="localhost:50051", beat="si"))


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
                f"Replicating '{request.current_replication}' of file '{request.file_name}"
            )
            request.current_replication += 1
            url = url_request(request.file_name)
            if url == "":
                return ccs_pb2.TransferResponse(message="end")
            with grpc.insecure_channel(url) as channel:
                stub = ccs_pb2_grpc.FileTransferServiceStub(channel)
                stub.TransferFile(request)

        return ccs_pb2.TransferResponse(message="File transfer complete.")


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ccs_pb2_grpc.add_FileTransferServiceServicer_to_server(
        FileTransferServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    # send_heartbeats_thread = Thread(target=send_heartbeats)
    # send_heartbeats_thread.daemon = True
    # send_heartbeats_thread.start()
    server.wait_for_termination()
