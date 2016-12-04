#!/usr/bin/env python
from sys import stdin
import re


def process(input):
    regex = re.compile('([\w]+)([\d]{3})\[([\w]{5})\]')
    sector_id_sum = 0

    for line in input.splitlines():
        m = regex.match(line.replace('-', ''))
        name, num, check = m.group(1), int(m.group(2)), m.group(3)
        if weighted_sort(name)[0:5] == check:
            sector_id_sum += num

    return sector_id_sum


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
