import math
def isPowerOfThree(n):
    if n <= 0: # 0 or negative numbers are not power of 3
        return False
    elif n == 1: # 3^0 = 1 so 1 is power of 3
        return True
    else: # if n is not 1 then divide n by 3 and check if the result is power of 3
        return isPowerOfThree(n / 3)

n = 27
print(isPowerOfThree(n)) # True