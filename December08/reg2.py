from sys import stdin
insts = [line.strip().split() for line in stdin.readlines()]
regs = {}
top = 0
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
    mod, cmd, num, oth, boo, chk = inst[0], inst[1], int(inst[2]), inst[4], inst[5], int(inst[6])
    if mod not in regs:
        regs[mod] = 0
    if oth not in regs:
        regs[oth] = 0
    regs[mod] += funcs[cmd](oth, num, boo, chk)
    top = max(list(regs.values()) + [top])
print(top)
