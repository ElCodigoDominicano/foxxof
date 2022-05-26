"""
* FOR DEMONSTRATIONAL PURPOSES ONLY *
A simple network device discovery tool

This is essentially asynchronous programming using threads to
execute the sniff function separately from sending the
"Magic String" -> MESSAGE to every host over the wire

another way is to use asyncio.. and changing the code up a bit.

-AERivas
"""
import ipaddress
import os
import socket
import struct
import sys
import threading
import time

SUBNET = input("Enter the subnet mask, Example => 192.168.0.0/24: ")
MESSAGE = input("Enter a message to send: ")

# could probably use class inheritance module here for ipaddress.
# Creating the IPs. header
class IP:

    def __init__(self, buff=None):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF
        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]
        # human readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # mapping protocol constants to its names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print(f'[!] {e} No protocol for -> {self.protocol_num}')
            self.protocol = str(self.protocol_num)

# Creating the ICMPs header
class ICMP:

    def __init__(self, buff):
        header = struct.unpack('<BBHHH', buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]


def udp_sender():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE, 'utf8'), (str(ip), 65212))

# Creating the discovery tool
class Scanner:
    def __init__(self, host):
        self.host = host
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == 'nt':
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    def sniff(self):
        # SET DATA TYPE
        hosts_up = {f"{str(self.host)} *"}

        try:
            while True: # that is... ICMP..
                # Read a packet
                raw_buffer = self.socket.recvfrom(65535)[0]
                # using the first 20 bytes create a IP header..
                ip_header = IP(raw_buffer[0:20])
                # output detected protocol and hosts
                if ip_header.protocol == "ICMP":
                    offset = ip_header.ihl * 4
                    buf = raw_buffer[offset:offset + 8]
                    icmp_header = ICMP(buf)
                    if icmp_header.code == 3 and icmp_header.type == 3:
                        if ipaddress.ip_address(ip_header.src_address) in ipaddress.IPv4Network(SUBNET):
                            if raw_buffer[len(raw_buffer) - len(MESSAGE):] == bytes(MESSAGE, 'utf8'):
                                tgt = str(ip_header.src_address)
                                if tgt != self.host and tgt not in hosts_up:
                                    hosts_up.add(str(ip_header.src_address))
                                    print(f"Host Up: {tgt}")

        # IF CTRL and or running windows turn of promiscuous mode
        except KeyboardInterrupt:
            if os.name == 'nt':
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

            print('\nUser Interrupted.')
            if hosts_up:
                print(f"\n\nSummary: Hosts up on {SUBNET}")
            for host in sorted(hosts_up):
                print(f"{host}")
            print('')
            sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = input("Enter The host => 192.168.0.107 <= Example: ")
    s = Scanner(host)

    # increase or decrease for less paranoid to paranoid
    print('[.]Going to sleep for 5 before the scanning starts')
    time.sleep(5)
    print("[*]Scanning for discoverable devices..")
    print('CTRL-C to exit')
    t = threading.Thread(target=udp_sender)
    t.start()
    s.sniff()
