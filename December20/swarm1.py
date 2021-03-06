from sys import stdin; import re
p, v, a, x, y, z = tuple(list(range(3)) + list(range(3)))
particles, parse = [line.strip().split(', ') for line in stdin.readlines()], re.compile(r'[^0-9,-]')
for i in range(len(particles)):
    particles[i] = [[int(k) for k in parse.sub('', particles[i][p]).split(',')],
                    [int(k) for k in parse.sub('', particles[i][v]).split(',')],
                    [int(k) for k in parse.sub('', particles[i][a]).split(',')]]
for _ in range(500):
    for i in range(len(particles)):
        for k in (x, y, z):
            particles[i][v][k] += particles[i][a][k]
            particles[i][p][k] += particles[i][v][k]
print(min(range(len(particles)), key=lambda j: sum(abs(particles[j][p][k]) for k in (x, y, z))))
