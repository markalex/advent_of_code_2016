#!/usr/bin/env python
from sys import stdin

keypad = {
    (0, 2): '1',
    (1, 1): '2',
    (1, 2): '3',
    (1, 3): '4',
    (2, 0): '5',
    (2, 1): '6',
    (2, 2): '7',
    (2, 3): '8',
    (2, 4): '9',
    (3, 1): 'A',
    (3, 2): 'B',
    (3, 3): 'C',
    (4, 2): 'D',
}


def process(input):
    pos = (2, 0)
    codez = []

    for line in input.splitlines():
        for cmd in line.strip():
            val = move(pos, cmd)
            if val in keypad:
                pos = val

        codez.append(keypad[pos])

    return ''.join(codez)


def move(location, dir):
    x, y = location

    if dir == "U":
        return (x-1, y)
    elif dir == "D":
        return (x+1, y)
    elif dir == "L":
        return (x, y-1)
    elif dir == "R":
        return (x, y+1)


print(process(stdin.read()))
