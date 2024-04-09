# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class NameNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/NameNode/Create',
                request_serializer=Service__pb2.CreateRequest.SerializeToString,
                response_deserializer=Service__pb2.CreateResponse.FromString,
                )
        self.ListFiles = channel.unary_unary(
                '/NameNode/ListFiles',
                request_serializer=Service__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=Service__pb2.ListFilesResponse.FromString,
                )
        self.ReplicationUrl = channel.unary_unary(
                '/NameNode/ReplicationUrl',
                request_serializer=Service__pb2.ReplicationUrlRequest.SerializeToString,
                response_deserializer=Service__pb2.ReplicationUrlResponse.FromString,
                )
        self.SaveNodeFile = channel.unary_unary(
                '/NameNode/SaveNodeFile',
                request_serializer=Service__pb2.SaveNodeFileRequest.SerializeToString,
                response_deserializer=Service__pb2.SaveNodeFileResponse.FromString,
                )
        self.DeleteNodeFile = channel.unary_unary(
                '/NameNode/DeleteNodeFile',
                request_serializer=Service__pb2.DeleteNodeFileRequest.SerializeToString,
                response_deserializer=Service__pb2.DeleteNodeFileResponse.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/NameNode/HeartBeat',
                request_serializer=Service__pb2.HeartBeatRequest.SerializeToString,
                response_deserializer=Service__pb2.HeartBeatResponse.FromString,
                )
        self.Download = channel.unary_unary(
                '/NameNode/Download',
                request_serializer=Service__pb2.DownloadRequest.SerializeToString,
                response_deserializer=Service__pb2.DownloadResponse.FromString,
                )


class NameNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicationUrl(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveNodeFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNodeFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=Service__pb2.CreateRequest.FromString,
                    response_serializer=Service__pb2.CreateResponse.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=Service__pb2.ListFilesRequest.FromString,
                    response_serializer=Service__pb2.ListFilesResponse.SerializeToString,
            ),
            'ReplicationUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicationUrl,
                    request_deserializer=Service__pb2.ReplicationUrlRequest.FromString,
                    response_serializer=Service__pb2.ReplicationUrlResponse.SerializeToString,
            ),
            'SaveNodeFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveNodeFile,
                    request_deserializer=Service__pb2.SaveNodeFileRequest.FromString,
                    response_serializer=Service__pb2.SaveNodeFileResponse.SerializeToString,
            ),
            'DeleteNodeFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNodeFile,
                    request_deserializer=Service__pb2.DeleteNodeFileRequest.FromString,
                    response_serializer=Service__pb2.DeleteNodeFileResponse.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=Service__pb2.HeartBeatRequest.FromString,
                    response_serializer=Service__pb2.HeartBeatResponse.SerializeToString,
            ),
            'Download': grpc.unary_unary_rpc_method_handler(
                    servicer.Download,
                    request_deserializer=Service__pb2.DownloadRequest.FromString,
                    response_serializer=Service__pb2.DownloadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/Create',
            Service__pb2.CreateRequest.SerializeToString,
            Service__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/ListFiles',
            Service__pb2.ListFilesRequest.SerializeToString,
            Service__pb2.ListFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicationUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/ReplicationUrl',
            Service__pb2.ReplicationUrlRequest.SerializeToString,
            Service__pb2.ReplicationUrlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveNodeFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/SaveNodeFile',
            Service__pb2.SaveNodeFileRequest.SerializeToString,
            Service__pb2.SaveNodeFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNodeFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/DeleteNodeFile',
            Service__pb2.DeleteNodeFileRequest.SerializeToString,
            Service__pb2.DeleteNodeFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/HeartBeat',
            Service__pb2.HeartBeatRequest.SerializeToString,
            Service__pb2.HeartBeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode/Download',
            Service__pb2.DownloadRequest.SerializeToString,
            Service__pb2.DownloadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DataNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPartition = channel.unary_unary(
                '/DataNode/SendPartition',
                request_serializer=Service__pb2.SendPartitionRequest.SerializeToString,
                response_deserializer=Service__pb2.SendPartitionResponse.FromString,
                )
        self.DownloadPartition = channel.unary_unary(
                '/DataNode/DownloadPartition',
                request_serializer=Service__pb2.DownloadPartitionRequest.SerializeToString,
                response_deserializer=Service__pb2.DownloadPartitionResponse.FromString,
                )
        self.Replicate = channel.unary_unary(
                '/DataNode/Replicate',
                request_serializer=Service__pb2.ReplicateRequest.SerializeToString,
                response_deserializer=Service__pb2.ReplicateResponse.FromString,
                )
        self.DeletePartition = channel.unary_unary(
                '/DataNode/DeletePartition',
                request_serializer=Service__pb2.DeletePartitionRequest.SerializeToString,
                response_deserializer=Service__pb2.DeletePartitionResponse.FromString,
                )


class DataNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendPartition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadPartition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Replicate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePartition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPartition': grpc.unary_unary_rpc_method_handler(
                    servicer.SendPartition,
                    request_deserializer=Service__pb2.SendPartitionRequest.FromString,
                    response_serializer=Service__pb2.SendPartitionResponse.SerializeToString,
            ),
            'DownloadPartition': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadPartition,
                    request_deserializer=Service__pb2.DownloadPartitionRequest.FromString,
                    response_serializer=Service__pb2.DownloadPartitionResponse.SerializeToString,
            ),
            'Replicate': grpc.unary_unary_rpc_method_handler(
                    servicer.Replicate,
                    request_deserializer=Service__pb2.ReplicateRequest.FromString,
                    response_serializer=Service__pb2.ReplicateResponse.SerializeToString,
            ),
            'DeletePartition': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePartition,
                    request_deserializer=Service__pb2.DeletePartitionRequest.FromString,
                    response_serializer=Service__pb2.DeletePartitionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendPartition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode/SendPartition',
            Service__pb2.SendPartitionRequest.SerializeToString,
            Service__pb2.SendPartitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadPartition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode/DownloadPartition',
            Service__pb2.DownloadPartitionRequest.SerializeToString,
            Service__pb2.DownloadPartitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Replicate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode/Replicate',
            Service__pb2.ReplicateRequest.SerializeToString,
            Service__pb2.ReplicateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePartition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode/DeletePartition',
            Service__pb2.DeletePartitionRequest.SerializeToString,
            Service__pb2.DeletePartitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
