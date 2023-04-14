from __future__ import annotations
from abc import ABC, abstractmethod


'''
    We use this pattern when we need a pipeline or
    chain of objects for processing a request
'''

class HttpRequest:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password


class Handler(ABC):
    def __init__(self, next: Handler) -> None:
        self.next = next
    
    def handle(self, request: HttpRequest):
        if self.do_handle(request):
            return

        if self.next != None:
            self.next.handle(request)
    
    @abstractmethod
    def do_handle(self, request: HttpRequest) -> bool:
        pass


class WebServer:
    def __init__(self, handler: Handler):
        self.handler = handler

    def handle(self, request: HttpRequest):
        self.handler.handle(request)


class Authenticator(Handler):
    def do_handle(self, request: HttpRequest) -> bool:
        is_valid = request.username == "admin" and request.password == "1234"
        print('Authentication')
        return not is_valid


class Compressor(Handler):
    def do_handle(self, request: HttpRequest):
        print('Compress')
        return False


class Logger(Handler):
    def do_handle(self, request: HttpRequest):
        print("Log")
        return False