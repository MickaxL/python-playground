#Client.py

# Client.py

import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

class ClientDnsMultiThread:

    def __init__(self, server_ip, server_port):

        self.server_addr = (server_ip, int(server_port))
        self.client_socket = socket(AF_INET, SOCK_DGRAM)

        print(f"Client prêt pour envoyer vers {server_ip} - {server_port}")


    def send_message(self, message):

        print(f"Envoi : {message}")
        self.client_socket.sendto(message.encode(), self.server_addr)

        data, addr = self.client_socket.recvfrom(1024)
        print(f"Réponse du serveur {addr} : {data.decode()}")


    def input_loop(self):

        while True:
            message = input("Entrer message : ")

            Thread(
                target=self.send_message,
                args=(message,)
            ).start()


client = ClientDnsMultiThread(sys.argv[1], sys.argv[2])
client.input_loop()