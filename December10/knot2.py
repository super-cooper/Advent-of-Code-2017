lengths = [ord(v) for v in input()] + [17, 31, 73, 47, 23]
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
print(''.join(('0' if not len(hex(x)[2:]) == 2 else '') + hex(x)[2:] for x in dense))
