#!/usr/bin/env python
from sys import stdin

keypad = {
    (0, 0): '1',
    (0, 1): '2',
    (0, 2): '3',
    (1, 0): '4',
    (1, 1): '5',
    (1, 2): '6',
    (2, 0): '7',
    (2, 1): '8',
    (2, 2): '9'
}


def process(input):
    pos = (1, 1)
    codez = []

    for line in input.splitlines():
        for cmd in line.strip():
            pos = move(pos, cmd)

        codez.append(keypad[pos])

    return ''.join(codez)


def move(location, dir):
    x, y = location

    if dir == "U":
        return (max(x-1, 0), y)
    elif dir == "D":
        return (min(x+1, 2), y)
    elif dir == "L":
        return (x, max(y-1, 0))
    elif dir == "R":
        return (x, min(y+1, 2))


print(process(stdin.read()))
