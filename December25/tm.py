import re; from sys import stdin
instructions, sub_int = [line.strip() for line in stdin.readlines() if line.strip() != ''], re.compile(r'[^0-9]')
def find_int(s): return int(sub_int.sub('', s))
machine, tape, q, stop, head = {}, {}, instructions[0][-2], find_int(instructions[1]), 0
for j, line in enumerate(instructions):
    if line.startswith('In'):
        state = line[-2]
        machine[state] = [[], []]
        for head in (0, 1):
            machine[state][head].append(find_int(instructions[j + 1]))
            machine[state][head].append(find_int(instructions[j + 2]))
            machine[state][head].append(1 if instructions[j + 3].endswith('right.') else -1)
            machine[state][head].append(instructions[j + 4].replace('.', '')[-1])
            j += 4
for _ in range(stop):
    if head not in tape:
        tape[head] = 0
    t = 0 if tape[head] == machine[q][0][0] else 1
    tape[head] = machine[q][t][1]
    head += machine[q][t][2]
    q = machine[q][t][3]
print(sum(tape[x] for x in tape))
