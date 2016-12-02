#!/usr/bin/env python
from sys import stdin

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def process(input):
    pos = (0, 0)
    dir = NORTH

    for cmd in input.split(', '):
        dir = turn(dir, cmd[0])
        pos = advance(dir, pos, int(cmd[1:]))

    return sum(map(abs, pos))


def turn(bearing, cmd):
    if cmd == "R":
        return (bearing + 1) % 4
    else:
        return (bearing - 1) % 4


def advance(b, coords, count):
    return {
        NORTH: lambda x: (x[0], x[1]+count),
        EAST: lambda x: (x[0]+count, x[1]),
        SOUTH: lambda x: (x[0], x[1]-count),
        WEST: lambda x: (x[0]-count, x[1])
    }[b](coords)

print(process(stdin.read()))
