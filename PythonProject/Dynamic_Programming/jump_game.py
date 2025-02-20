def canJump(nums):
    if len(nums) == 1: # that means you are already at the destination
        return True
    dest = len(nums) - 1 # destination is the last index of nums
    for i in range(len(nums) - 2, -1, -1): # start from last but one element and move forward
        if i + nums[i] >= dest: # if i which is the start point and num[i] which is the max jump >= dest index
            dest = i # change the dest index to current index as now going forward our aim is to reach
                     # this particular index

    return True if dest == 0 else False