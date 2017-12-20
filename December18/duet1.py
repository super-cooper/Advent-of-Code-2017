from sys import stdin, exit
insts = [line.strip().split() for line in stdin.readlines()]
i, last, regs, funcs = 0, 0, {}, {
    0: (lambda f, x, y: funcs[f](funcs[1](x), funcs[1](y))), 1: (lambda k: k if type(k) is int else regs[k]),
    "add": (lambda x, y: x + y), "mul": (lambda x, y: x * y), "mod": (lambda x, y: x % y)
}
while i < len(insts):
    inst = insts[i]
    func, mod, other = inst[0], int(inst[1]) if inst[1].lstrip('-').isdigit() else inst[1], \
        (int(inst[2]) if inst[2].lstrip('-').isdigit() else regs[inst[2]]) if len(inst) > 2 else None
    if type(mod) is str and mod not in regs:
        regs[mod] = 0
    if func == "snd":
        last = funcs[1](mod)
    elif func == "set":
        regs[mod] = funcs[1](other)
    elif func == "rcv":
        if funcs[1](mod) != 0:
            print(last)
            exit(0)
    elif func == "jgz":
        i += 0 if funcs[1](mod) <= 0 else funcs[1](other) - 1
    else:
        regs[mod] = funcs[0](func, mod, other)
    i += 1
