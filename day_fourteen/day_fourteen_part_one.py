#!/usr/bin/env python
from sys import argv
import hashlib
import re


def process(input):
    triple = re.compile(r'((\w)\2{2,})')
    match_count = 0
    i = -1

    while match_count < 64:
        i += 1
        hash = hashlib.md5(input + str(i))
        hex = hash.hexdigest()

        m = triple.findall(hex)
        if m:
            char = m[0][1]
            reg = '(([' + char + ']{5}))'
            q = re.compile(reg)
            for j in range(i+1, i+1000):
                hash = hashlib.md5(input + str(j))
                hex = hash.hexdigest()
                x = q.findall(hex)
                if x:
                    match_count += 1
                    continue

    return i


print(process(str(argv[1])))
