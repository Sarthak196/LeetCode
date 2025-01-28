import math
def minEatingSpeed(piles, h):
    l, r = 1, max(piles) # l is the minimum speed that is 1, r is the maximum speed which is the maximum number of bananas in a pile
    res = r # res is the result which let it be the max speed
    while l <= r: # perform binary search to find te minimum speed between 1 to max(piles)
        k = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += math.ceil(p / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res

piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles, h))