from sys import stdin
import re
from collections import defaultdict


def process(input):
    goes_to_re = re.compile(r'value (\d+) goes to bot (\d+)')
    gives_re = re.compile(
        r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')

    bots = defaultdict(set)
    outputs = defaultdict(set)
    processed = set()

    lines = input.splitlines()

    while len(processed) < len(lines):
        for line in lines:

            if line in processed:
                continue

            values = goes_to_re.match(line)
            if values:
                val, bot = map(int, values.groups())
                bots[bot].add(val)
            else:
                source, l_dest_type, l_dest, h_dest_type, h_dest
                = gives_re.match(line).groups()

                chips = bots[int(source)]

                if len(chips) < 2:
                    continue

                lower = min(chips)
                higher = max(chips)

                lower_dest = outputs if l_dest_type == 'output' else bots
                higher_dest = outputs if h_dest_type == 'output' else bots

                lower_dest[int(l_dest)].add(min(chips))
                higher_dest[int(h_dest)].add(max(chips))

            processed.add(line)

    return list(outputs[0])[0] * list(outputs[1])[0] * list(outputs[2])[0]


print(process(stdin.read()))
