import socket

def check_port(host, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((host, port))
    sock.close

    return result == 0

host = "google.com"       # modify
port = 22                 # modify 

if check_port(host, port):
    print(f"Port {port} is open on {host}")
else:
    print("Port already used or server unreachable")