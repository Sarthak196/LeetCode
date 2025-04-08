def can_jump(nums):
    dest = len(nums) - 1 # The last index is the destination
    for i in range(len(nums) - 2, -1, -1): # Start from the second last index and go backwards
        if i + nums[i] >= dest: # If the current index can reach the destination
            dest = i # Update the destination to the current index
    return True if dest == 0 else False # If we can reach the first index, return True

# Test cases
print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
