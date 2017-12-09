total, score, garb, neg = 0, 0, False, False
for c in input():
    if c == '{' and not garb:
        score += 1
    elif c == '}' and not garb:
        total += score
        score -= 1
    elif c == '<' and not garb:
        garb = True
    elif c == '>' and not neg:
        garb = False
    elif c == '!' and garb:
        neg = not neg
    elif neg:
        neg = False
print(total)
