#!/usr/bin/env python
from sys import stdin
import re


def process(input):
    count = 0

    for line in input.splitlines():
        found = False
        inside = re.findall(r'\[(.+?)]', line)

        for y in inside:
            found = found or hasPalindrome(y)

        if not found:
            outside = re.split(r'\[(.+?)]', line)
            for a in outside:
                if hasPalindrome(a):
                    count += 1
                    break

    return count


def is_valid(m):
    (x, y) = m
    return x != y


def hasPalindrome(list):
    palindrome_regex = re.compile(r'(?=(\w)(\w)\2\1)')
    return any(is_valid(m) for m in palindrome_regex.findall(list))


print(process(stdin.read()))
