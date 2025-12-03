from itertools import groupby
import textwrap

running_total = 0

def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

with open('input.txt', 'r') as file:
    ranges = file.read().strip().split(',')
    for r in ranges:
        start, end = r.split('-')
        for i in range(int(start), int(end) + 1):
            for j in range(1, len(str(i))):
                substrings = textwrap.wrap(str(i), j)
                if all_equal(substrings):
                    running_total += i
                    break
    print(running_total)