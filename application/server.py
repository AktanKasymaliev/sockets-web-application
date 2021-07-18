import socket 
from abc import abstractmethod

from application.render import render_to_string
from application.decorators import handle_exceptions
from application.logger_cfg import LoggingConfig

class BaseServer:

    """ Interface for Server """

    @abstractmethod
    def __set_logging(self): pass

    @abstractmethod
    def run(self): pass

    @abstractmethod
    def _send_response(self): pass

class Server(BaseServer):

    HOST = "localhost"
    PORT = 8000

    @handle_exceptions
    def __init__(self) -> None:
        # Set logger
        self.logger = LoggingConfig(__name__).log
        # Set up server protocol or rules
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind server to this address
        self.server_socket.bind (
            (self.HOST, self.PORT)
            )

        self.logger.info('Starting server on localhost 8000')
        self.logger.info('The Web server URL for this would be http://localhost:8000/')
        # Listening incoming requests
        self.server_socket.listen()

    def render_request(self, request):
        request_method = request[:15]
        return request_method

    @handle_exceptions
    def run(self) -> None:
        # Run and handle/send client movements
        self.logger.info('Entering infinite loop; hit CTRL-C to exit\n')
        while True:
            # Wait for an incoming connection.
            client_socket, (client_host, client_port) = self.server_socket.accept()
            self.request = client_socket.recv(1024).decode("utf-8")
            # Get request method from str
            request_method = self.render_request(self.request)
            self.logger.info(request_method)
            # Send html template/response
            self._send_response(client_socket)

    @handle_exceptions
    def _send_response(self, client_socket: socket.socket) -> None:

        # Sending to the server html reponse
        client_socket.sendall(
        str.encode("HTTP/1.1 200 OK\n"
         + "Content-Type: text/html\n"
         + "\n" # Important!
         + render_to_string("page.html")
         )
        )

        # Close connection after sended response 
        client_socket.close()

