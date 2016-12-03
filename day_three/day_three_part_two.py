#!/usr/bin/env python
from sys import stdin


def process(input):
    count = 0
    rows = [map(int, [line[i:i+5] for i in range(0, len(line), 5)])
            for line in input.splitlines()]

    triangles = []
    for i in range(0, len(rows), 3):
        for j in range(3):
            triangles.append(sorted([rows[i][j], rows[i+1][j], rows[i+2][j]]))

    return len([item for item in triangles if item[0] + item[1] > item[2]])

print(process(stdin.read()))
