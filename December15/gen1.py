from sys import stdin; import re
stuff = [re.sub(r'[^0-9]', '', line.strip()) for line in stdin.readlines()]
a, b, count, cmp = int(stuff[0]), int(stuff[1]), 0, 0xffff
for _ in range(40_000_000):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & cmp == b & cmp:
        count += 1
print(count)
