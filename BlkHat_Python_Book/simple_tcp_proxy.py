import sys
import socket
import threading

# for each integer in the range of 0 to 255, if the length of the corresponding
# character equals 3, we get the character ( chr(i)). Otherwise, we get a dot
# ( .). Then we join that list into a string
# Gives the first 256 integers
HEX_FILTER = ''.join([(len(repr(chr(i)))==3) and chr(i) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    # grab a piece of the string to dump and put it into the word variable
    if isinstance(src, bytes):
        src = src.decode()

    results = list()
    for i in range(0, len(src), length):
        word = str(src[i:i+length])
        
        # the translate built-in function to substitute the string
        # representation of each character for the corresponding character in the raw
        # string ( printable )
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02x}' for c in word])
        hexwidth = length * 3
        
        # we substitute the hex representation of the
        # integer value of every character in the raw string ( hexa). Finally, we create a
        # new array to hold the strings, result, that contains the hex value of the index
        # of the first byte in the word, the hex value of the word, and its printable rep-
        # resentation
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results
# To recieve local and remote data.
def receive_from(connection):
    buffer = b""
    
    # By default, we set a five-second time-out, which
    # might be aggressive if you’re proxying traffic to other countries or over lossy
    # networks, so increase the time-out as necessary
    connection.settimeout(5)
    try:
        while True:
            #  set up a loop to read response data into the buffer until nothing can be read
            data = connection.recv(4096)
            if not data:
                break
            buffer += data
    except Exception as e:
        #print(f"Exception was.. {e} passing....")
        pass
    # This buffer cna be either local machine or remote
    return buffer


"""
Inside these functions, you can modify the packet contents, perform
fuzzing tasks, test for authentication issues, or do whatever else your heart
desires. This can be useful, for example, if you find plaintext user creden-
tials being sent and want to try to elevate privileges on an application by
passing in admin instead of your own username.
"""
def request_handler(buffer):
    # To perform packet modifications.
    return buffer

def response_handler(buffer):
    # To perform packet modifications.
    return buffer

""" The Follwing function contains the bulk logic of the program """

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    # Start by creating and connecting to the remote host
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    # Check to make sure we dont need to first initiate a connection to the remote side and quest data
    # Some server daemons will expect you to do this FTP servers typically send a banner first....
    
    # using receive_from for both remote and client communications.
    # It accepts a connected socket object and performs a receive
    # Dump the contents of the packet and pass the output to response_handler
    if receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)
    
    remote_buffer = response_handler(remote_buffer)
    if len(remote_buffer):
        print("[<==] Sending %d bytes to localhost." % len(remote_buffer))
        client_socket.send(remote_buffer)
    
    while True:
        local_buffer = receive_from(client_socket)
        if len(local_buffer):
            line = "[==>] Received %d bytes from localhost." % len(local_buffer)
            print(line)
            hexdump(local_buffer)
            local_buffer = response_handler(local_buffer)
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote.")
        
        remote_buffer = receive_from(remote_socket)    
        if len(remote_buffer):
            print("[<==] Received %d in bytes from remote." % len(remote_buffer))
            hexdump(remote_buffer)
            remote_buffer = response_handler(remote_buffer)
            client_socket.send(remote_buffer)
            print("[<==] Sent to localhost.")

        if not len(local_buffer) and not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    # create a socket and binds it to the local host and listens..
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((local_host, local_port))
    except Exception as e:
        print('[!] Problem on bind: %r' % e)
        
        print("[!!] Failed to listen on %s:%d" % (local_host,local_port))
        print("[!!] Check for other listening sockets or correct permissions.")
        sys.exit[0]
    print("[*] Listening on %s:%d" %(local_host, local_port))
    server.listen(5)
    
    # when fresh connection requests come in we hand it off to the proxy_handler in a new thread
    # which does all of the sending and receiving of juicy bits to either side of the data stream
    while True:
        client_socket, addr = server.accept()
        # print out the local connection information
        line = "> Received incomming connection from %s:%d" % (addr[0], addr[1])
        print(line)
        # Start a thread to talk to the remote host
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()

def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: ./simple_tcp_proxy.py [localhost] [localport]", end=' ')
        print("[remotehost] [remoteport] [receive_first]")
        print("Example: ./simple_tcp_proxy.py 127.0.0.1 9000 3.13.23.1 9000 True")
        sys.exit(0)
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

if __name__ == '__main__':
    main()