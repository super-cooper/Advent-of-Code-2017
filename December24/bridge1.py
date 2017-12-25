from sys import stdin
ports = set(tuple(map(int, p)) for p in [line.split('/') for line in stdin.readlines()])
def strongest(arr, curr, last, used, best):
    strength = sum(sum(p) for p in curr)
    best = strength if strength > best else best
    for port in arr:
        if last[1 - used] in port:
            new = arr.copy()
            new.remove(port)
            best = strongest(new, curr + [port], port, 0 if port[0] in last else 1, best)
    return best
print(strongest(ports, [], (0, 0), 0, 0))
