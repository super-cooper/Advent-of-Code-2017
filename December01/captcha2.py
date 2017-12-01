puzzle = [int(v) for v in [c for c in input()]]
print(2 * sum(puzzle[i] if puzzle[i] == puzzle[i + (len(puzzle) // 2)] else 0 for i in range(len(puzzle) // 2)))
