removed, garb, neg = 0, False, False
for c in input():
    if c == '<' and not garb:
        garb = True
    elif c == '>' and not neg:
        garb = False
    elif c == '!' and garb:
        neg = not neg
    elif garb and c != '>' and not neg:
        removed += 1
    elif neg:
        neg = False
print(removed)
