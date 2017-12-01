puzzle = [int(v) for v in [c for c in input()]]
print(sum(puzzle[i] if puzzle[i] == (puzzle[i + 1] if i < len(puzzle) - 1 else puzzle[0]) else 0
          for i in range(len(puzzle))))
