#!/usr/bin/python3
""" validUTF8 function """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0
    for byte in data:
        byte = toBinary(byte)
        if num_bytes == 0:
            if byte[0] == '0':
                continue
            elif byte[:3] == '110':
                num_bytes = 1
            elif byte[:4] == '1110':
                num_bytes = 2
            elif byte[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if not byte.startswith('10'):
                return False
            num_bytes -= 1
            if num_bytes < 0:
                return False
    return num_bytes == 0


def toBinary(num):
    if num == 0:
        return '0'
    binary = ''
    count = 0
    while count < 8:
        binary = str(num % 2) + binary
        num = num // 2
        count += 1
    return binary
