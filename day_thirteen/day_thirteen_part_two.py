#!/usr/bin/env python
from sys import argv


def process(input):
    visited = {(1, 1)}
    current = {(1, 1)}
    steps = 0

    while True:
        v = current.copy()
        current = set()
        for x, y in v:
            for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if a < 0 or b < 0:
                    continue
                if is_wall(a, b, input):
                    continue
                if (a, b) in visited:
                    continue
                visited.add((a, b))
                current.add((a, b))
        steps += 1

        if steps == 50:
            return len(visited)


def is_wall(x, y, n):
    calc = (x*x + 3*x + 2*x*y + y + y*y) + n
    ones = bin(calc).count('1')
    return (ones % 2) == 1


print(process(int(argv[1])))
