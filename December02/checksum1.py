from sys import stdin
print(sum(max(int(v) for v in row) - min(int(v) for v in row) for row in
          [line.replace('\n', '').split() for line in stdin.readlines()]))
