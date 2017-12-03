vals = {(0, 0): 1}
val = 0
row = 1
x = 0
y = 0
target = int(input())


def sum_adj(x, y):
    return sum(
        [vals[(x - 1, y)] if (x - 1, y) in vals else 0,
         vals[(x, y - 1)] if (x, y - 1) in vals else 0,
         vals[(x + 1, y)] if (x + 1, y) in vals else 0,
         vals[(x, y + 1)] if (x, y + 1) in vals else 0,
         vals[(x + 1, y - 1)] if (x + 1, y - 1) in vals else 0,
         vals[(x - 1, y - 1)] if (x - 1, y - 1) in vals else 0,
         vals[(x + 1, y + 1)] if (x + 1, y + 1) in vals else 0,
         vals[(x - 1, y + 1)] if (x - 1, y + 1) in vals else 0])


while val == 0:
    while x < row:
        x += 1
        vals[(x, y)] = sum_adj(x, y)
        if vals[(x, y)] > target and val == 0:
            val = vals[(x, y)]
    while y < row:
        y += 1
        vals[(x, y)] = sum_adj(x, y)
        if vals[(x, y)] > target and val == 0:
            val = vals[(x, y)]
    while x > -row:
        x -= 1
        vals[(x, y)] = sum_adj(x, y)
        if vals[(x, y)] > target and val == 0:
            val = vals[(x, y)]
    while y > -row:
        y -= 1
        vals[(x, y)] = sum_adj(x, y)
        if vals[(x, y)] > target and val == 0:
            val = vals[(x, y)]
    row += 1

print(val)
