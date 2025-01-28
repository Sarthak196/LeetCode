def threeSumClosest(nums, target):
    nums.sort()
    minval = float('inf')
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            k = a + nums[l] + nums[r]
            minval = min(minval, abs(target-k))
            if k > target:
                r -= 1
            elif k < target:
                l += 1
            else:
                return target
    return minval+target

nums = [0,0,0]
target = 1
print(threeSumClosest(nums, target)) # 2