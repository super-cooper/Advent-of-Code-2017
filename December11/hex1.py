end = [0, 0, 0]
for step in [step for step in input().split(',')]:
    if 's' == step:
        end[1] -= 1
        end[2] += 1
    elif 'n' == step:
        end[1] += 1
        end[2] -= 1
    elif 'ne' == step:
        end[0] += 1
        end[2] -= 1
    elif 'nw' == step:
        end[0] -= 1
        end[1] += 1
    elif 'se' == step:
        end[0] += 1
        end[1] -= 1
    else:
        end[0] -= 1
        end[2] += 1
print(max(abs(coord) for coord in end))
