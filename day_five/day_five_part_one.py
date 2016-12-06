#!/usr/bin/env python
from sys import argv
import hashlib


def process(input):
    code = []
    i = -1
    while len(code) < 8:
        i += 1
        hash = hashlib.md5(input + str(i))
        hex = hash.hexdigest()

        if hex[0:5] == '00000':
            code.append(hex[5])

    return ''.join(code)


print(process(str(argv[1])))
