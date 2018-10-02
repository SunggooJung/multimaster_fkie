# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import file_pb2 as file__pb2


class FileServiceStub(object):
  """* The launch manager service definition. 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFileContent = channel.unary_stream(
        '/FileService/GetFileContent',
        request_serializer=file__pb2.GetFileContentRequest.SerializeToString,
        response_deserializer=file__pb2.GetFileContentReply.FromString,
        )
    self.SaveFileContent = channel.stream_stream(
        '/FileService/SaveFileContent',
        request_serializer=file__pb2.SaveFileContentRequest.SerializeToString,
        response_deserializer=file__pb2.SaveFileContentReply.FromString,
        )
    self.Rename = channel.unary_unary(
        '/FileService/Rename',
        request_serializer=file__pb2.RenameRequest.SerializeToString,
        response_deserializer=file__pb2.ReturnStatus.FromString,
        )
    self.ListPath = channel.unary_unary(
        '/FileService/ListPath',
        request_serializer=file__pb2.ListPathRequest.SerializeToString,
        response_deserializer=file__pb2.ListPathReply.FromString,
        )
    self.ListPackages = channel.unary_unary(
        '/FileService/ListPackages',
        request_serializer=file__pb2.ListPackagesRequest.SerializeToString,
        response_deserializer=file__pb2.ListPackagesReply.FromString,
        )


class FileServiceServicer(object):
  """* The launch manager service definition. 
  """

  def GetFileContent(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SaveFileContent(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Rename(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPath(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPackages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFileContent': grpc.unary_stream_rpc_method_handler(
          servicer.GetFileContent,
          request_deserializer=file__pb2.GetFileContentRequest.FromString,
          response_serializer=file__pb2.GetFileContentReply.SerializeToString,
      ),
      'SaveFileContent': grpc.stream_stream_rpc_method_handler(
          servicer.SaveFileContent,
          request_deserializer=file__pb2.SaveFileContentRequest.FromString,
          response_serializer=file__pb2.SaveFileContentReply.SerializeToString,
      ),
      'Rename': grpc.unary_unary_rpc_method_handler(
          servicer.Rename,
          request_deserializer=file__pb2.RenameRequest.FromString,
          response_serializer=file__pb2.ReturnStatus.SerializeToString,
      ),
      'ListPath': grpc.unary_unary_rpc_method_handler(
          servicer.ListPath,
          request_deserializer=file__pb2.ListPathRequest.FromString,
          response_serializer=file__pb2.ListPathReply.SerializeToString,
      ),
      'ListPackages': grpc.unary_unary_rpc_method_handler(
          servicer.ListPackages,
          request_deserializer=file__pb2.ListPackagesRequest.FromString,
          response_serializer=file__pb2.ListPackagesReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'FileService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class FileClientServiceStub(object):
  """* The client for launch manager service to receive notifications about file changes. 
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FileChange = channel.stream_unary(
        '/FileClientService/FileChange',
        request_serializer=file__pb2.ChangedFile.SerializeToString,
        response_deserializer=file__pb2.Empty.FromString,
        )


class FileClientServiceServicer(object):
  """* The client for launch manager service to receive notifications about file changes. 
  """

  def FileChange(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FileClientServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FileChange': grpc.stream_unary_rpc_method_handler(
          servicer.FileChange,
          request_deserializer=file__pb2.ChangedFile.FromString,
          response_serializer=file__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'FileClientService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
