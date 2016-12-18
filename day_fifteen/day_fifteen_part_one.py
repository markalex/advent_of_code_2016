#!/usr/bin/env python

tdiscs = [
    [4, 0, 1, 2, 3],
    [1, 0]
]

discs = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0],
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 0, 1],
    [1, 2, 3, 4, 5, 6, 0],
    [3, 4, 0, 1, 2],
    [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4]
]


def process():
    i = 0
    while True:
        j = i
        vals = []
        for d in discs:
            j += 1
            vals.append(d[j % len(d)])

        if sum(vals) == 0:
            return i
        i += 1

print(process())
