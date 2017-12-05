from sys import stdin
insts = [int(v) for v in [line.strip() for line in stdin.readlines()]]
i = 0
steps = 0
while 0 <= i < len(insts):
    inst = insts[i]
    insts[i] += 1
    i += inst
    steps += 1
print(steps)
