#Server.py

import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

class ServerDnsMultiThread:

    def __init__(self, ip, port):

        self.server_socket = socket(AF_INET, SOCK_DGRAM)
        self.server_socket.bind(ip, int(port))
        print(f"DNS waiting at {ip} - {port}")

    def handle_client(self, data, client_addr):
        message = data.decode()
        print(f"Message reçu de {client_addr} : {message}")

        self.server_socket.sendto("OK".encode(), client_addr)
    
    def listen_loop(self):
        while True:
            data, client_addr = self.server_socket.recvfrom(1024)
            Thread(
                target=self.handle_client,
                args=(data, client_addr)
            ).start()
            print(f"Client Connected : {client_addr}")

server = ServerDnsMultiThread(sys.argv[1], sys.argv[2])
server.listen_loop()