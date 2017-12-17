steps, buf, curr, val, k = int(input()), [0], 0, 0, 0
while k < 50_000_000:
    i = (k - curr) // steps
    k += i + 1
    curr = ((curr + ((i + 1) * (steps + 1)) - 1) % k) + 1
    val = k if curr == 1 else val
print(val)
