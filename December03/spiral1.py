n = int(input())
coord = (0, 0)
i = 1
x = 0
y = 0
row = 1

while i < n:
    while x < row:
        x += 1
        i += 1
        if i == n:
            coord = (x, y)
    while y < row:
        y += 1
        i += 1
        if i == n:
            coord = (x, y)
    while x > -row:
        x -= 1
        i += 1
        if i == n:
            coord = (x, y)
    while y > -row:
        y -= 1
        i += 1
        if i == n:
            coord = (x, y)
    row += 1

print(abs(coord[0]) + abs(coord[1]))
