moves, programs = input().split(','), [chr(x) for x in range(ord('a'), ord('q'))]
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
print(''.join(programs))
