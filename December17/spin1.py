steps, buf, curr = int(input()), [0], 0
for k in range(1, 2018):
    curr = ((curr + steps) % len(buf)) + 1
    buf.insert(curr, k)
print(buf[curr + 1 if curr < len(buf) - 1 else 0])
