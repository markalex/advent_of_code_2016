#!/usr/bin/env python
from sys import stdin
import re


def process(input):
    trio = re.compile(r'(?=(\w)(\w)(\1))')
    count = 0

    for line in input.splitlines():
        inside = re.split(r'\[.+?]', line)
        outside = re.findall(r'\[(.+?)]', line)

        in_matches = [item for sublist in
                      [trio.findall(x) for x in inside]
                      for item in sublist]
        out_matches = [item for sublist in
                       [trio.findall(y) for y in outside]
                       for item in sublist]

        count += any(m for m in in_matches
                     for n in out_matches
                     if is_legit(m) and inverse(m) == n)

    return count


def is_legit(x):
    (a, b, _) = x
    return a != b


def inverse(x):
    (a, b, _) = x
    return (b, a, b)


print(process(stdin.read()))
