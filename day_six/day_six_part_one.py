#!/usr/bin/env python
from sys import stdin
import operator


def process(input):
    letters = []
    word = []

    for line in input.splitlines():
        for i in range(len(line)):
            c = line[i]
            if len(letters) < len(line):
                letters.append({c: 1})
            else:
                if c in letters[i]:
                    letters[i][c] += 1
                else:
                    letters[i][c] = 1

    for i in range(len(letters)):
        word.append(
            sorted(letters[i].items(),
                   key=operator.itemgetter(1),
                   reverse=True)[0][0])

    return ''.join(word)


print(process(stdin.read()))
