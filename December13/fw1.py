from sys import stdin
print(sum(l[0] * l[1] if ((l[0] + 1) % (l[1] - 1) == 1) else 0 for l in
          [tuple(int(v) for v in l.split(': ')) for l in stdin.readlines()]))
