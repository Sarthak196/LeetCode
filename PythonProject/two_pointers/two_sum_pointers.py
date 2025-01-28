def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while r >= l: # place the two pointers at the start and end of the list
        if numbers[r] + numbers[l] > target: # if the sum of the two numbers is greater than the target, move the right pointer to the left
            r -= 1
        elif numbers[r] + numbers[l] < target: # if the sum of the two numbers is less than the target, move the left pointer to the right
            l += 1
        else:
            return [l, r]

numbers = [1,2,3,4]
target = 3
print(twoSum(numbers, target))