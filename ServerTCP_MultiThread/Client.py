#client.py
# client.py

import sys
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


class TcpClient:

    def __init__(self, ip, port):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((ip, int(port)))
        print(f"connected to server at {ip} on {port}")

    def send_loop(self):
        while True:
            message = input("message : ")

            if not message:
                continue

            if message == "quit":
                break

            self.client_socket.send(message.encode())

            data = self.client_socket.recv(2048)

            if not data:
                break

            print(f"server response : {data.decode()}")

        self.client_socket.close()


client = TcpClient(sys.argv[1], sys.argv[2])
client.send_loop()