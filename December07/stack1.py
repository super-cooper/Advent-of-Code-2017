from sys import stdin
import re
children = {re.sub(r'\([0-9]+\)', '', line[0]).strip(): set(line[1:]) for line in
            [re.split(r' -> |, ', line.strip()) for line in stdin.readlines()]}
nodes = lambda n: 1 + sum(nodes(c) for c in children[n])
print([prog for prog in children if nodes(prog) == len(children)][0])
