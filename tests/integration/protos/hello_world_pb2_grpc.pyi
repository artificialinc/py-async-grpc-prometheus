"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import collections.abc
import grpc
import tests.integration.protos.hello_world_pb2

class GreeterStub:
    """The greeting service definition."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    SayHello: grpc.UnaryUnaryMultiCallable[
        tests.integration.protos.hello_world_pb2.HelloRequest,
        tests.integration.protos.hello_world_pb2.HelloReply,
    ]
    """Sends a greeting."""
    SayHelloUnaryStream: grpc.UnaryStreamMultiCallable[
        tests.integration.protos.hello_world_pb2.MultipleHelloResRequest,
        tests.integration.protos.hello_world_pb2.HelloReply,
    ]
    """Sends one greeting, get multiple response."""
    SayHelloStreamUnary: grpc.StreamUnaryMultiCallable[
        tests.integration.protos.hello_world_pb2.HelloRequest,
        tests.integration.protos.hello_world_pb2.HelloReply,
    ]
    """Send multiple greetings, get one response."""
    SayHelloBidiStream: grpc.StreamStreamMultiCallable[
        tests.integration.protos.hello_world_pb2.MultipleHelloResRequest,
        tests.integration.protos.hello_world_pb2.HelloReply,
    ]
    """Send multiple greetings, get multiple response."""

class GreeterServicer(metaclass=abc.ABCMeta):
    """The greeting service definition."""

    @abc.abstractmethod
    def SayHello(
        self,
        request: tests.integration.protos.hello_world_pb2.HelloRequest,
        context: grpc.ServicerContext,
    ) -> tests.integration.protos.hello_world_pb2.HelloReply:
        """Sends a greeting."""
    @abc.abstractmethod
    def SayHelloUnaryStream(
        self,
        request: tests.integration.protos.hello_world_pb2.MultipleHelloResRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[tests.integration.protos.hello_world_pb2.HelloReply]:
        """Sends one greeting, get multiple response."""
    @abc.abstractmethod
    def SayHelloStreamUnary(
        self,
        request_iterator: collections.abc.Iterator[tests.integration.protos.hello_world_pb2.HelloRequest],
        context: grpc.ServicerContext,
    ) -> tests.integration.protos.hello_world_pb2.HelloReply:
        """Send multiple greetings, get one response."""
    @abc.abstractmethod
    def SayHelloBidiStream(
        self,
        request_iterator: collections.abc.Iterator[tests.integration.protos.hello_world_pb2.MultipleHelloResRequest],
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[tests.integration.protos.hello_world_pb2.HelloReply]:
        """Send multiple greetings, get multiple response."""

def add_GreeterServicer_to_server(servicer: GreeterServicer, server: grpc.Server) -> None: ...
