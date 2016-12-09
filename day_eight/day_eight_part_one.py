#!/usr/bin/env python
from sys import stdin
import re

NUM_COLS = 50
NUM_ROWS = 6


def process(input):
    screen = grid(NUM_ROWS, NUM_COLS)
    rotate_re = re.compile(r'(?:\w+) (\w+) (?:[xy]=)(\d+) by (\d+)')
    rect_re = re.compile(r'(?:\w+) (\d+)x(\d+)')

    for line in input.splitlines():
        rotate_match = rotate_re.match(line)
        if rotate_match:
            dir, start, length = rotate_match.groups()
            if dir == 'row':
                screen = rotate_row(screen, int(start), int(length))
            else:
                screen = rotate_col(screen, int(start), int(length))
        else:
            rect_match = rect_re.match(line)
            if rect_match:
                rows, cols = rect_match.groups()
                screen = rect(screen, int(rows), int(cols))

    return count(screen, NUM_ROWS, NUM_COLS)


def rotate_row(grid, start, length):
    row = grid[start]
    size = len(row)
    new = list(row)
    for i in range(size):
        index = (i + length) % size
        new[index] = row[i]
    grid[start] = new

    return grid


def rotate_col(grid, start, length):
    size = len(grid)
    new = []
    for i in range(size):
        new.append(grid[i][start])

    for i in range(size):
        index = (i + length) % size
        grid[index][start] = new[i]

    return grid


def count(grid, rows, cols):
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            cnt += grid[i][j]
    return cnt


def rect(grid, cols, rows):
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 1

    return grid


def grid(rows, cols):
    g = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        g.append(row)
    return g


print(process(stdin.read()))
