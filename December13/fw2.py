from sys import stdin
layers = [tuple(int(v) for v in l.split(': ')) for l in stdin.readlines()]
delay = 0
while any((l[0] + delay) % ((l[1] - 1) * 2) == 0 for l in layers):
    delay += 1
print(delay)
