#!/usr/bin/env python
from sys import stdin
import re
import string


def process(input):
    regex = re.compile('([\w-]+)-([\d]{3})\[([\w]{5})\]')
    rooms = []

    for line in input.splitlines():
        m = regex.match(line)
        name, num, check = m.group(1), int(m.group(2)), m.group(3)
        if weighted_sort(name.replace('-', ''))[0:5] == check:
            decrypted = ''.join([decrypt(y, num) for y in name])
            if decrypted == 'northpole object storage':
                return num


def decrypt(char, num):
    if char == '-':
        return ' '
    return string.lowercase[(string.lowercase.index(char) + num) % 26]


def weighted_sort(input):
    dict = {}
    for c in sorted(input):
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    return ''.join([e[0] for e in
                   sorted(dict.items(), key=lambda x: (-x[1], x[0]))])


print(process(stdin.read()))
