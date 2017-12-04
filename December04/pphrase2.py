from sys import stdin
print(sum(len(set(''.join(sorted(word)) for word in line)) == len(line) for line in [line.replace('\n', '').split()
                                                                                     for line in stdin.readlines()]))
