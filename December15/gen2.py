from sys import stdin; import re
stuff = [re.sub(r'[^0-9]', '', line.strip()) for line in stdin.readlines()]
a, b, count, cmp = int(stuff[0]), int(stuff[1]), 0, 0xffff
for _ in range(5_000_000):
    while True:
        a = (a * 16807) % 2147483647
        if a % 4 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b % 8 == 0:
            break
    if a & cmp == b & cmp:
        count += 1
print(count)
