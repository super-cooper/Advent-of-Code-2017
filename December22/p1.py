from sys import stdin
grid = [line.strip() for line in stdin.readlines()]
pos = [len(grid) // 2, len(grid[0]) // 2]
status, cur, inf = {}, (-1, 0), 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        status[(i, j)] = grid[i][j]
for _ in range(10_000):
    if tuple(pos) not in status:
        status[tuple(pos)] = '.'
    if status[tuple(pos)] == '#':
        status[tuple(pos)] = '.'
        cur = (cur[1], -cur[0])
    else:
        status[tuple(pos)] = '#'
        inf += 1
        cur = (-cur[1], cur[0])
    pos[0] += cur[0]
    pos[1] += cur[1]
print(inf)
