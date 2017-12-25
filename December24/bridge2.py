from sys import stdin
ports = set(tuple(map(int, p)) for p in [line.split('/') for line in stdin.readlines()])
def strongest(arr, curr, last, used, bridges):
    bridges.append(curr)
    for port in arr:
        if last[1 - used] in port:
            new = arr.copy()
            new.remove(port)
            strongest(new, curr + [port], port, 0 if port[0] in last else 1, bridges)
    return bridges
perms = strongest(ports, [], (0, 0), 0, [])
best = max(len(b) for b in perms)
print(sum(sum(p) for p in max([b for b in perms if len(b) == best], key=lambda b: sum(sum(p) for p in b))))
