"""
just another netcat replacement.

colorized....
"""
import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

class NetCat:
    # Initialize netcat object from the command line and the buffer
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        # Create socket_object
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Entry point for NetCat, manages the NetCat object
    def run(self):
        # Are we setting up as a listener.
        if self.args.listen:
            self.listen()
        # Otherwise we are sending.
        else:
            self.send()
    # Sender method (This is used in the run function above.)
    def send(self):
        # Create connection object using target IP and PORT.
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        # Manually close connection using CTRL + C.
        try:
            # Start loop to recieve data from the target until no more data.
            while True:
                recv_len = 1
                response = ''
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    # If there is no more data break out of the loop.
                    if recv_len < 4096:
                        break
                # Print response and pause to give an interactive input, send that input and continue the loop.
                if response:
                    print(response)
                    buffer = input('> ')
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except EOFError as EOF:
            print(EOF,"Going to pass..")
            pass
        # Loop until CTRL+C user termination..
        except KeyboardInterrupt:
            print('User Terminated.')
            self.socket.close()
            sys.exit()
    # Listener method (This is used in the run function above.)
    def listen(self):
        # Starts a bind using the targets IP and PORT and starts a Listening Loop.
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        while True:
            client_socket, _ = self.socket.accept()
            # Passes connected socket to the handle method
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()
    # The Logic for an interactive shell, file uploads and command execution.
    def handle(self, client_socket):
        # If command execution, all command executions are handled..and all outputs are sent back to the socket.
        if self.args.execute:
            output = execute(self.args.execute)
            client_socket.send(output.encode())
        # Else if uploads, all upload commands are handled.
        elif self.args.upload:
            file_buffer = b''
            # Loop listening socket
            while True:
                data = client_socket.recv(4096)
                # Accumulate data
                if data:
                    file_buffer += data
                # End if no data can be accumulated
                else:
                    break
                # Write accumulated data to specified file.
                with open(self.args.upload, 'wb') as f:
                    f.write(file_buffer)
                message = f'Saved file {self.args.upload}'
                client_socket.send(message.encode())
        # If interactive shell
        elif self.args.command:
            cmd_buffer = b''
            # Loop an interactive shell socket. and run the execute function and return the output to sender.
            while True:
                """ 
                You’ll notice that the shell scans for a newline character to determine
                when to process a command, which makes it netcat friendly. That is, you can
                use this program on the listener side and use netcat itself on the sender side.
                However, if you’re conjuring up a Python client to speak to it, remember to
                add the newline character. In the send method, you can see we do add the
                newline character after we get input from the console.
                """
                try:
                    client_socket.send(b'JANCT: $01> ')
                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b''

                except Exception as e:
                    print(f'server killed {e} ')
                    self.socket.close()
                    sys.exit()
    
# Runs a command on the local system and returns that output.
def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)

    return output.decode()

# Handles command line arguments and the rest of the functions
if __name__ == '__main__':
    """
    The -c argument sets up an interactive shell, the -e
    argument executes one specific command, the -l argument indicates that
    a listener should be set up, the -p argument specifies the port on which to
    communicate, the -t argument specifies the target IP, and the -u argument
    specifies the name of a file to upload. Both the sender and receiver can
    use this program, so the arguments define whether it’s invoked to send or
    listen. The -c, -e, and -u arguments imply the -l argument, because those
    arguments apply to only the listener side of the communication. The sender
    side makes the connection to the listener, and so it needs only the -t and -p
    arguments to define the target listener. 
    """
    # Argparse library is  used to create a command line interface (or program in this case)
    parser = argparse.ArgumentParser(
        description='Just Another Network Communication Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        epilog=textwrap.dedent('''Example:
        net_cat.py -t 192.168.0.113 -p 5555 -l -c # command shell
        net_cat.py -t 192.168.0.113 -p 5555 -l -u=mytest.txt # upload to file
        net_cat.py -t 192.168.0.113 -p 5555 -l -e=\"cat /etc/passwd\" # execute command
        echo 'ABC' | ./netcat.py -t 192.168.0.113 -p 135 # echo text to server port 135
        net_cat.py -t 192.168.0.113 -p 5555 # connect to server
        '''))
    # Argument creation.
    parser.add_argument('-c', '--command' ,action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='excecute specified command')
    parser.add_argument('-l', '--listen', action='store_true', help='listen')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    parser.add_argument('-t', '--target', default='192.168.0.113', help='specified IP')
    parser.add_argument('-u', '--upload', help='upload file')
    # If we are to set up as a listener else set up as a sender.
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    # Set up to run.
    nc = NetCat(args, buffer.encode())
    nc.run()