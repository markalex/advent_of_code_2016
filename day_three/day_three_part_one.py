#!/usr/bin/env python
from sys import stdin


def process(input):
    count = 0
    for line in input.splitlines():
        sides = sorted(map(int, [line[i:i+5] for i in range(0, len(line), 5)]))
        if sides[0] + sides[1] > sides[2]:
            count += 1

    return count


print(process(stdin.read()))
