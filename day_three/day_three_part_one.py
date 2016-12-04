#!/usr/bin/env python
from sys import stdin


def process(input):
    count = 0
    for line in input.splitlines():
        sides = sorted([int(n) for n in line.split()])

        if sum(sides[0:2]) > sides[2]:
            count += 1

    return count


print(process(stdin.read()))
