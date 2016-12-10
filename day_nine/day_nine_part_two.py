#!/usr/bin/env python
from sys import stdin
from itertools import *
import re


def process(input):
    return _calc(iter(input))


def _calc(g):
    m_regex = re.compile(r'(\d+)x(\d+)')
    count = 0

    while True:
        try:
            txt = list(takewhile(lambda x: x != '(', g))
            count += len(txt)
            m = ''.join(takewhile(lambda x: x != ')', g))
            a, b = m_regex.match(m).groups()
            count += _calc(islice(g, int(a))) * int(b)
        except:
            break

    return count


print(process(stdin.read()))
