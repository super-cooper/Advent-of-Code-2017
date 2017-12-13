from sys import stdin
print(sum(layer[0] * layer[1] if ((layer[0] + 1) % (layer[1] - 1) == 1) else 0 for layer in
          [tuple(int(v) for v in l.split(': ')) for l in stdin.readlines()]))
