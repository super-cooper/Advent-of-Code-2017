from sys import stdin
insts = [line.strip().split() for line in stdin.readlines()]
regs = {}
for inst in insts:
    mod, cmd, num, oth, boo, chk = inst[0], inst[1], int(inst[2]), inst[4], inst[5], int(inst[6])
    if mod not in regs:
        regs[mod] = 0
    if oth not in regs:
        regs[oth] = 0
    do = False
    exec('do = {} {} {}'.format(regs[oth], boo, chk))
    regs[mod] += (num if cmd == 'inc' else -num) if do else 0
print(regs[max(regs, key=lambda x: regs[x])])
