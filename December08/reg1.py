from sys import stdin
insts = [line.strip().split() for line in stdin.readlines()]
regs = {}
funcs = {
    'inc': (lambda reg, amt, how, cmp: amt if funcs[how](regs[reg], cmp) else 0),
    'dec': (lambda reg, amt, how, cmp: -funcs['inc'](reg, amt, how, cmp)),
    '<':   (lambda x, y: x < y),
    '>':   (lambda x, y: x > y),
    '==':  (lambda x, y: x == y),
    '<=':  (lambda x, y: x <= y),
    '>=':  (lambda x, y: x >= y),
    '!=':  (lambda x, y: x != y)
}
for inst in insts:
    mod = inst[0]
    cmd = inst[1]
    num = int(inst[2])
    oth = inst[4]
    boo = inst[5]
    chk = int(inst[6])
    if mod not in regs:
        regs[mod] = 0
    if oth not in regs:
        regs[oth] = 0
    regs[mod] += funcs[cmd](oth, num, boo, chk)
print(regs[max(regs, key=lambda x: regs[x])])
