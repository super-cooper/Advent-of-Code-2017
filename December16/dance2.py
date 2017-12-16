from collections import OrderedDict; import sys
moves, programs, found, its = input().split(','), [chr(x) for x in range(ord('a'), ord('q'))], OrderedDict(), 10 ** 9
for k in range(its):
    for move in moves:
        do = move[0]
        if do == 's':
            x = int(move[1:])
            tmp = programs[-x:]
            programs = programs[:-x]
            programs = tmp + programs
        elif do == 'x':
            i, j = tuple(int(x) for x in move[1:].split('/'))
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp
        elif do == 'p':
            p1, p2 = tuple(move[1:].split('/'))
            i, j = programs.index(p1), programs.index(p2)
            tmp = programs[i]
            programs[i] = programs[j]
            programs[j] = tmp
        res = ''.join(programs)
    if res in found:
        print(list(found.keys())[(its % k) - 1])
        sys.exit(0)
    found[res] = None
