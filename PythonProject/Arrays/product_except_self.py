def productExceptSelf(nums):
    l = [1]
    r = [1]
    length = len(nums)
    for i in range(length - 1):
        l.append(l[i] * nums[i]) # calculate the product of the numbers to the left of the current number [1,1,2,8]
    for i in range(length - 1, 0, -1):
        r.append(r[length-1-i] * nums[i]) # calculate the product of the numbers to the right of the current number [1,6,24,48]
    res = []
    for i in range(length):
        res.append(l[i] * r[length -1 - i])  # multiply the product of the numbers to the left and reverse of
                                             # right of the current number
    return res

nums = [1,2,4,6]
print(productExceptSelf(nums)) # [48, 24, 12, 8]