#!/usr/bin/env python
from sys import stdin


def process(input):
    rows = []

    for line in input.splitlines():
        rows.append([int(n) for n in line.split()])

    triangles = []
    for i in range(0, len(rows), 3):
        for j in range(3):
            triangles.append(sorted([rows[i][j], rows[i+1][j], rows[i+2][j]]))

    return len([item for item in triangles if sum(item[0:2]) > item[2]])

print(process(stdin.read()))
