from sys import stdin
lines = [line.replace('\n', '').split() for line in stdin.readlines()]
total = 0
for row in lines:
    for i in range(len(row)):
        v1 = int(row[i])
        for v2 in [int(c) for c in row[i + 1:]]:
            if (v1 / v2).is_integer():
                total += v1 / v2
            elif (v2 / v1).is_integer():
                total += v2 / v1
print(int(total))
