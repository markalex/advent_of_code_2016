#!/usr/bin/env python
from sys import stdin

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def process(input):
    return move((0, 0), NORTH, [], input.split(', '))


def move(pos, dir, visited, commands):
    dir = turn(dir, commands[0][0])

    for i in range(int(commands[0][1:])):
        pos = advance(dir, pos, 1)

        if pos in visited:
            return sum(map(abs, pos))

        visited.append(pos)

    return move(pos, dir, visited, commands[1:])


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
