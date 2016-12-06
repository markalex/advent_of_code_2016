#!/usr/bin/env python
from sys import argv
import hashlib


def process(input):
    code = {}
    i = -1
    while len(code) < 8:
        i += 1
        hash = hashlib.md5(input + str(i))
        hex = hash.hexdigest()

        if hex[0:5] == '00000':
            pos = hex[5]
            if pos in '01234567' and int(pos) not in code:
                code[int(pos)] = hex[6]

    return ''.join([e[1] for e in sorted(code.items())])


print(process(str(argv[1])))
