#server.py

import sys
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class TcpServerMultiThread:
    
    def __init__(self, ip, port):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((ip, int(port)))
        self.server_socket.listen()
        print(f"waiting for connection at {ip} on {port}")
    
    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(2048)
            if not data:
                break
        
            message = data.decode()
            print(f"message : {message}")

            client_socket.send("OK".encode())

        client_socket.close()
    
    def listen_loop(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            Thread(target=self.handle_client, args=(client_socket,)).start()
            print(f"Client connected on {client_addr}")

server = TcpServerMultiThread(sys.argv[1], sys.argv[2])
server.listen_loop()
