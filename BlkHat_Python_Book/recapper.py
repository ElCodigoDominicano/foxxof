"""
a simple pcap analyzer.
"""
from scapy.all import TCP, rdpcap
import collections
import os
import re
import sys
import zlib

OUTDIR = '/home/foxhound/Desktop/pictures'
PCAPS = '/home/foxhound/BH_Python (current)'

# Similar to a regular tuple except this can access fields through their names (somewhat like a dictionary)
# unlike a dictionary this makes it more memory-efficient.
Response = collections.namedtuple('Response', ['header' , 'payload'])

def get_header(payload):
    """
     Returns http headers from raw HTTP traffic

     - extracts header by looking for the portion of the payload
     - that starts at the beginning and ends with a couple of carriage return and newline pairs
     - if payload doesn't match the pattern it will raise a value error which will pass a '-'
     - creates a dictionary of the header
     - if no header information is found None will be given.

    Parameter payload:  a string containing the header information to be extracted
    """
    try:
        header_raw = payload[:payload.index(b'\r\n\r\n')+2]
    except ValueError:
        sys.stdout.write('-')
        sys.stdout.flush()
        return None

    header = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', header_raw.decode()))
    if 'Content-Type' not in header:
        return None
    return header

def extract_content(Response, content_name='image'):
    """
     Returns the content and content_type
     - if the content has been encoded..
     -
     -
     -
    Parameter Response: namedtuple with 'header' and 'payload' information.
    Parameter content_name: if content-type contains image or not (default: image)
    """

    content, content_type = None, None
    if content_name in Response.header['Content-Type']:
        content_type = Response.header['Content-Type'].split('/')[1]
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]
        if 'Content-Encoding' in Response.header:
            if Response.header['Content-Encoding'] == "gzip":
                content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Content-Encoding'] == "deflate":
                content = zlib.decompress(Response.payload)
    return content, content_type


class Recapper:
    def __init__(self, fname):
        pcap = rdpcap(fname)
        self.sessions = pcap.sessions()
        self.responses = list()

    def get_responses(self):
        for session in self.sessions:
            #print(session)
            payload = b''
            for packet in self.sessions[session]:
                try:
                    if packet[TCP].dport == 80   or packet[TCP].sport == 80:
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    sys.stdout.write('x')
                    sys.stdout.flush()
            if payload:
                header = get_header(payload)
                if header is None:
                    continue
                self.responses.append(Response(header=header, payload=payload))

    def write(self, content_name):
        for i, response in enumerate(self.responses):
            content, content_type = extract_content(response, content_name)
            if content and content_type:
                fname = os.path.join(OUTDIR, f'ex{i}.{content_type}')
                print(f'Writing {fname}')
                with open(fname, 'wb') as f:
                    f.write(content)

if __name__ == '__main__':
    pfile = os.path.join(PCAPS, 'arper.pcap')
    recapper = Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')
