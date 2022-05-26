"""
a simple user datagram protocol (udp) discovery tool.
win / *nix

Windows requires us to set some additional flags through a socket input/output control (IOCTL),
which enables promiscuous mode on the network interface An input/output
control (IOCTL) is a means for user space programs to communicate with
kernel mode components. - PG.37

improve by adding nmap scans to check exploitations, attack surfaces..

this sniffs only one paacket
"""


import socket
import os

HOST = input("Enter target IP [fmt => xxx.xxx.xxx.xxx]: ")

def main():
    # Create raw socket for windows if target machine is windows otherwise *nix
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST,0))
    # include ip header to capture
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # IF windows turn on promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    # read one packet
    print(sniffer.recvfrom(65565))
    # IF windows turn off promiscuous mode
    if os.name == 'nt':
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
if __name__ == '__main__':
    main()