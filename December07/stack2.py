from sys import stdin
import re
from statistics import mode
progs = [re.split(r' -> |, ', line.strip()) for line in stdin.readlines()]
children = {re.sub(r'\([0-9]+\)', '', line[0]).strip(): line[1:] for line in progs}
weights = {re.sub(r'\([0-9]+\)', '', line[0]).strip(): int(re.search(r'([0-9]+)', line[0]).group(0)) for line in progs}
partials = {}
def sum_weights(s):
    partials[s] = weights[s] + sum(sum_weights(t) if t not in partials else partials[t] for t in children[s])
    return partials[s]
for prog in children:
    sum_weights(prog)
unbal = lambda s: not all(partials[ch] == partials[children[s][0]] for ch in children[s])
nodes = lambda n: 1 + sum(nodes(c) for c in children[n])
root = [prog for prog in children if nodes(prog) == len(children)][0]
final = root
while any(unbal(child) for child in children[final]):  # Search the tree for the final unbalanced node
    for child in children[final]:
        if unbal(child):
            final = child
            break
desired = mode([partials[c] for c in children[final]])
example = [ch for ch in children[final] if partials[ch] == desired][0]
broken = [ch for ch in children[final] if partials[ch] != desired][0]
print(weights[broken] + (partials[example] - partials[broken]))
