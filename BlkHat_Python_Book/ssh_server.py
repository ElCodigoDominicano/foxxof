""" 
Simple SSH2 server socket using Paramiko 

Any commands typed into the SSH Server * The machine running  ssh_server.py *
are sent to the SSH Client * The machine running ssh_rcmd.py*

SSH Server ---> [Sending Commands] ---> SSH Client
SSH Server <--- [Receiving Output] <--- SSH Client
"""

import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
# This hostkey is included in the paramiko demo files..
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))

class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'fox') and (password == 'alphatest'):
            return paramiko.AUTH_SUCCESSFUL

if __name__ == '__main__':
    server = '192.168.0.107'
    ssh_port = 2222
    # Creating the socket listener ... and 'ssh'-ing that socket.
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[*] Listening for connection ...')
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed: ' + str(e))
        sys.exit(1)
    else:
        print('[+] Got a connection!', client, addr)
    # Creating the client. and configure the authentication method for the client.
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(HOSTKEY)

    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)
    # Once authenticated
    print('[*] Authenticated!')
    # receives a 'Client Connected' Message
    print(chan.recv(1024))
    chan.send('Welcome to Fox<->ssh')
    try:
        while True:
            command = input("Enter command: ")
            if command != 'exit':
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode)
            else:
                chan.send('exit')
                print('[!] Exiting ...')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()

