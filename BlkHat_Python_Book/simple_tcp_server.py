"""
A simple TCP server.

- FoX
"""
import socket
import threading

def serv(ip, port):
    """
    - AF_INET indicates to make use of the standard IPv4 address or host name
    - SOCK_STREAM indicates this will be TCP versed
    - Binds a connection to the specified ip and port for the server
    - Listens for a connection on specified port
    - Accepts the connection

    Parameter ip: str an IPv4 address
    Parameter port: int a network port number
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f"[*] Listening on {ip}:{port}")

    while True:
        client, address = server.accept()
        print(f"[*] Accepted Connection from {address[0]}:{address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    """
    - Recieves data being sent to the server
    - Sends data in bytes ; back to the client

    Parameter client_socket: obj a client_socket object 
    """
    print(f"This is client_socket ->{client_socket}")
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[*] Received: {request.decode('utf-8')}")
        sock.send(b"ACK")

if __name__ == '__main__':
    ip = input('Enter an ip to use: ')
    port = int(input('Enter the port to use: '))
    serv(ip, port)