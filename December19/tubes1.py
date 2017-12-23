from sys import stdin
tubes = [line.replace('\n', '') for line in stdin.readlines()]
j, i, res, n, s, e, w = tubes[0].index('|'), 0, '', (0, -1), (0, 1), (1, 0), (-1, 0)
curr = s
while True:
    new_i, new_j = i, j
    if tubes[i][j].isalpha():
        res += tubes[i][j]
    for d in [curr] + [d for d in (n, s, e, w) if d != curr]:
        new_i, new_j = i + d[1], j + d[0]
        if (0 <= new_i < len(tubes)) and (0 <= new_j < len(tubes[new_i])) and not tubes[new_i][new_j].isspace():
            if ((curr in (n, s) and d in (e, w) and tubes[new_i][new_j] in ('|', '+'))
                    or (curr in (e, w) and d in (n, s) and tubes[new_i][new_j] in ('-', '+'))
                    or ((d in ((-curr[0], curr[1]), (curr[0], -curr[1])) or tubes[i][j].isalpha()) and d != curr)):
                new_i, new_j = i, j
                continue
            curr = d
            break
    if new_i == i and new_j == j or tubes[new_i][new_j].isspace():
        break
    i, j = new_i, new_j
print(res)
