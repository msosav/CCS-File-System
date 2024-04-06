# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ccs_pb2 as ccs__pb2


class FileTransferServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TransferFile = channel.unary_unary(
                '/FileTransferService/TransferFile',
                request_serializer=ccs__pb2.TransferRequest.SerializeToString,
                response_deserializer=ccs__pb2.TransferResponse.FromString,
                )
        self.GetUrl = channel.unary_unary(
                '/FileTransferService/GetUrl',
                request_serializer=ccs__pb2.urlRequest.SerializeToString,
                response_deserializer=ccs__pb2.urlResponse.FromString,
                )


class FileTransferServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TransferFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileTransferServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TransferFile': grpc.unary_unary_rpc_method_handler(
                    servicer.TransferFile,
                    request_deserializer=ccs__pb2.TransferRequest.FromString,
                    response_serializer=ccs__pb2.TransferResponse.SerializeToString,
            ),
            'GetUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUrl,
                    request_deserializer=ccs__pb2.urlRequest.FromString,
                    response_serializer=ccs__pb2.urlResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileTransferService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileTransferService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TransferFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileTransferService/TransferFile',
            ccs__pb2.TransferRequest.SerializeToString,
            ccs__pb2.TransferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileTransferService/GetUrl',
            ccs__pb2.urlRequest.SerializeToString,
            ccs__pb2.urlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)