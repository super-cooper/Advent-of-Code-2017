def knot(string):
    lengths = [ord(v) for v in string] + [17, 31, 73, 47, 23]
    nums = list(range(256))
    curr = 0
    skip = 0
    for _ in range(64):
        for l in lengths:
            if l > len(nums):
                continue
            i = curr
            j = (curr + l - 1) % len(nums)
            for __ in range(l // 2):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i = (i + 1) % len(nums)
                j = (j - 1) % len(nums)
            curr = (curr + l + skip) % len(nums)
            skip += 1

    def xor_all(i):
        tot = nums[i]
        for j in range(i + 1, i + 16):
            tot ^= nums[j]
        return tot

    dense = [xor_all(i) for i in range(0, len(nums), 16)]
    code = ''.join(('0' if not len(hex(x)[2:]) == 2 else '') + hex(x)[2:] for x in dense)
    return int('0x' + code, 16)


grid = []
start = input()
for i in range(128):
    row = [0] * 128
    tie = knot(start + '-{}'.format(i))
    mask = 2 ** 127
    j = 0
    while mask > 0:
        bit = tie & mask
        row[j] = 1 if bit > 0 else 0
        mask >>= 1
        j += 1
    grid.append(row)
group = 2


def fill_group(i, j, group):
    if grid[i][j] == 0 or grid[i][j] > 1:
        return
    up, down, left, right = 0, 0, 0, 0
    if i > 0:
        up = grid[i - 1][j]
    if j > 0:
        left = grid[i][j - 1]
    if i < len(grid) - 1:
        down = grid[i + 1][j]
    if j < len(grid) - 1:
        right = grid[i][j + 1]
    for v in (up, down, left, right):
        if v > 1:
            grid[i][j] = v
            break
    if grid[i][j] == 1:
        grid[i][j] = group
    if i > 0:
        fill_group(i - 1, j, group)
    if j > 0:
        fill_group(i, j - 1, group)
    if i < len(grid) - 1:
        fill_group(i + 1, j, group)
    if j < len(grid) - 1:
        fill_group(i, j + 1, group)


for i in range(len(grid)):
    for j in range(len(grid)):
        fill_group(i, j, group)
        if grid[i][j] == group:
            group += 1
print(group - 2)
