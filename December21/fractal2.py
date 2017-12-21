from sys import stdin; from copy import deepcopy
rules = {tuple(r[:r.find(' ')].split('/')): r[r.find('=> ') + 3:].strip().split('/') for r in
         [line.strip() for line in stdin.readlines()]}
for rule in list(rules.keys()):
    r = deepcopy(rule)
    for _ in range(4):
        rules[tuple(v[::-1] for v in r)] = rules[rule]
        r = tuple(''.join(v) for v in zip(*r[::-1]))
        rules[r] = rules[rule]
img = [".#.", "..#", "###"]
for _ in range(18):
    enhanced = []
    div = 2 if len(img[0]) % 2 == 0 else 3
    for x in range(len(img[0]) // div):
        for y in range(len(img) // div):
            p = []
            for yi in range(y * div, (y * div) + div):
                sub = ''
                for xi in range(x * div, (x * div) + div):
                    sub += img[yi][xi]
                p.append(sub)
            p = tuple(p)
            for i, row in enumerate(rules[p]):
                if y * len(rules[p]) + i >= len(enhanced):
                    enhanced.append('')
                enhanced[y * len(rules[p]) + i] += row
    img = enhanced
print(sum(s.count('#') for s in img))
