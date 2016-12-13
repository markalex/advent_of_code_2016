#!/usr/bin/env python
from sys import stdin


def process(input):
    # set c == 1 for part two, 0 for part one
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    instructions = input.splitlines()
    i = 0

    while i < len(instructions):
        cmd = instructions[i].split()
        if cmd[0] == 'cpy':
            if cmd[1].isdigit():
                registers[cmd[2]] = int(cmd[1])
            else:
                registers[cmd[2]] = registers[cmd[1]]
            i += 1
        elif cmd[0] == 'inc':
            registers[cmd[1]] += 1
            i += 1
        elif cmd[0] == 'dec':
            registers[cmd[1]] -= 1
            i += 1
        elif cmd[0] == 'jnz':
            test = int(cmd[1]) if cmd[1].isdigit() else registers[cmd[1]]
            if test != 0 and i < len(instructions):
                i = i + int(cmd[2])
            else:
                i += 1

    return registers['a']


print(process(stdin.read()))
