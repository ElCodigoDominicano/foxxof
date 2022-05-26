"""
* FOR DEMONSTRATIONAL PURPOSES ONLY *
A simple TCP client. Returns some decoded data

- AERivas
"""
import socket

def tcp_client(target_host, target_port):
    """
    - AF_INET indicates to make use of the standard IPv4 address or host name
    - SOCK_STREAM indicates this will be a TCP Client
    - Creates a connection to the client server
    - Sends data as bytes to the client server
    - Recieves some data then decodes this data
    - Returns decoded data after connection is severed

    Parameter target_host: str containing the provided IPv4 address
    Parameter target_port: int containing the port number to be used
    """   
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.connect((target_host, target_port))
    socket_object.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    response = socket_object.recv(4096)
    
    decoded = response.decode()
    socket_object.close()

    return decoded

if __name__ == '__main__':
    target_host = input('Enter the targets ip address: ')
    target_port = int(input('Enter the port to use: '))
    tcp_client(target_host, target_port)