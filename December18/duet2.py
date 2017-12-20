from sys import stdin, exit
insts = [line.strip().split() for line in stdin.readlines()]
i, sent, regs, funcs = [0, 0], 0, ({'p': 0}, {'p': 1}), {
    0: (lambda f, pid, x, y: funcs[f](funcs[1](x, pid), funcs[1](y, pid))),
    1: (lambda k, pid: k if type(k) is int else regs[pid][k]),
    "add": (lambda x, y: x + y), "mul": (lambda x, y: x * y), "mod": (lambda x, y: x % y)
}
q, waiting, p = ([], []), [False, False], 1
while i[0] < len(insts) and i[1] < len(insts) and not (waiting[p] and waiting[p - 1]):
    p = 1 - p
    inst = insts[i[p]]
    func, mod, other = inst[0], int(inst[1]) if inst[1].lstrip('-').isdigit() else inst[1], \
        (int(inst[2]) if inst[2].lstrip('-').isdigit() else regs[p][inst[2]]) if len(inst) > 2 else None
    if type(mod) is str and mod not in regs[p]:
        regs[p][mod] = 0
    if func == "snd":
        q[1 - p].append(funcs[1](mod, p))
        if p == 1:
            sent += 1
    elif func == "set":
        regs[p][mod] = funcs[1](other, p)
    elif func == "rcv":
        if not len(q[p]) == 0:
            regs[p][mod] = q[p].pop(0)
            waiting[p] = False
        else:
            waiting[p] = True
    elif func == "jgz":
        i[p] += 0 if funcs[1](mod, p) <= 0 else funcs[1](other, p) - 1
    else:
        regs[p][mod] = funcs[0](func, p, mod, other)
    i[p] += 0 if waiting[p] else 1
print(sent)
