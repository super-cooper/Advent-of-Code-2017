lengths = [int(v) for v in input().split(',')]
nums = list(range(256))
curr = 0
skip = 0
for l in lengths:
    if l > len(nums):
        continue
    i = curr
    j = (curr + l - 1) % len(nums)
    for _ in range(l // 2):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        i = (i + 1) % len(nums)
        j = (j - 1) % len(nums)
    curr = (curr + l + skip) % len(nums)
    skip += 1
print(nums[0] * nums[1])
