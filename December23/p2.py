from sys import stdin
insts = [line.strip().split() for line in stdin.readlines()]
i, regs, funcs = 0, {'a': 1}, {
    0: (lambda f, x, y: funcs[f](funcs[1](x), funcs[1](y))), 1: (lambda k: k if type(k) is int else regs[k]),
    "add": (lambda x, y: x + y), "mul": (lambda x, y: x * y), "mod": (lambda x, y: x % y), "sub": (lambda x, y: x - y)
}
p, q, h, v = 0, 0, 0, 0
while i < len(insts):
    inst = insts[i]
    func, mod, other = inst[0], int(inst[1]) if inst[1].lstrip('-').isdigit() else inst[1], \
        (int(inst[2]) if inst[2].lstrip('-').isdigit() else regs[inst[2]]) if len(inst) > 2 else None
    if type(mod) is str and mod not in regs:
        regs[mod] = 0
    if func == "mul":
        regs[mod] = funcs[0](func, mod, other)
    elif func == "set":
        regs[mod] = funcs[1](other)
    elif func == "jnz":
        i += 0 if funcs[1](mod) == 0 else funcs[1](other) - 1
    else:
        regs[mod] = funcs[0](func, mod, other)
    i += 1
    if mod == 'f':
        p = regs['b']
        q = regs['c']
        v = -int(insts[len(insts) - 2][2])
        break
for r in range(p, q + 1, v):
    for i in range(2, r):
        if r % i == 0:
            h += 1
            break
print(h)
