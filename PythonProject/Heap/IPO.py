import heapq
def findMaximizedCapital(k, w, profits, capital):
    n = len(profits)
    projects = [(capital[i], profits[i]) for i in range(n)]
    projects.sort() # sort the projects based on capital on ascending order
    maxheap = []
    i = 0
    for _ in range(k): # iterate k times as k is the number of resources
        while i < n and projects[i][0] <= w: # find all projects that can be done with the current capital
            heapq.heappush(maxheap, -projects[i][1]) # push the negative profit to maxheap as we want max profit
            i += 1 # move to the next project
        if not maxheap: # if there are no projects that can be done with the current capital break the loop
            break
        w -= heapq.heappop(maxheap) # add the profit to the capital by using - as we pushed negative profit
    return w

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(findMaximizedCapital(k, w, profits, capital)) # 4

# time complexity: O(nlogn + klogn) = O((n+k)logn)

"""
Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
"""
