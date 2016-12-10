#!/usr/bin/env python
from sys import stdin
from itertools import *
import re


def process(input):
    count = 0
    m_regex = re.compile(r'(\d+)x(\d+)')

    g = iter(input)
    while True:
        try:
            txt = list(takewhile(lambda x: x != '(', g))
            count += len(txt)
            m = ''.join(takewhile(lambda x: x != ')', g))
            a, b = m_regex.match(m).groups()
            segment_length = len(list(islice(g, int(a))))
            count += (segment_length * int(b))
        except:
            break

    return count


print(process(stdin.read()))
