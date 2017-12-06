blocks = [int(v) for v in input().strip().split()]
seen = set()
curr = tuple(v for v in blocks)
steps = 0
while curr not in seen:
    seen.add(curr)
    largest = max(range(len(blocks)), key=lambda k: blocks[k])
    i = min([k for k in range(len(blocks)) if blocks[k] == blocks[largest]])
    hold = blocks[i]
    blocks[i] = 0
    while hold > 0:
        i = i + 1 if (i != len(blocks) - 1) else 0
        blocks[i] += 1
        hold -= 1
    steps += 1
    curr = tuple(blocks[j] for j in range(len(blocks)))
print(steps)
