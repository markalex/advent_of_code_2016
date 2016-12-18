#!/usr/bin/env python
from sys import argv
import hashlib
import re

d = {}


def process(input):
    triple = re.compile(r'((\w)\2{2,})')
    match_count = 0
    i = -1

    while match_count < 64:
        i += 1
        hex = hash_2016(input + str(i))
        m = triple.findall(hex)
        if m:
            char = m[0][1]
            reg = '(([' + char + ']{5}))'
            q = re.compile(reg)
            for j in range(i+1, i+1000):
                hex = hash_2016(input + str(j))
                x = q.findall(hex)
                if x:
                    match_count += 1
                    continue

    return i


def hash_2016(input):
    if input in d:
        return d[input]
    hash = hashlib.md5(input)
    hex = hash.hexdigest()
    for i in range(2016):
        hash = hashlib.md5(hex)
        hex = hash.hexdigest()

    d[input] = hex
    return hex

print(process(str(argv[1])))
