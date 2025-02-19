def climbStairs(n):
    no_of_ways = [0,1] # this is the base case
    for i in range(2, n+2): # start from 2 so that i-2 is valid
        no_of_ways.append(no_of_ways[i-2]+no_of_ways[i-1]) # always the ans is sum of previous two ways
    return no_of_ways[n+1]

print(climbStairs(4))

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the stairs