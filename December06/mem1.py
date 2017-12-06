blocks = [int(v) for v in input().strip().split()]
configs = {i: v for i, v in enumerate(blocks)}
seen = set()
curr = tuple(v for v in blocks)
steps = 0
while curr not in seen:
    seen.add(curr)
    largest = max(range(len(blocks)), key=lambda k: configs[k])
    i = min([k for k in configs.keys() if configs[k] == configs[largest]])
    hold = configs[i]
    configs[i] = 0
    while hold > 0:
        i = i + 1 if (i != len(blocks) - 1) else 0
        configs[i] += 1
        hold -= 1
    steps += 1
    curr = tuple(configs[j] for j in range(len(blocks)))
print(steps)
