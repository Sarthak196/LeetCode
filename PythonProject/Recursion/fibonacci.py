def fib(n):
    if n == 0:  # base case are taken for 0 and 1 so that n-1 and n-2 will not go in negative
        return 0
    elif n == 1:
        return 1
    else: # if n is not 0 or 1 then return the sum of n-1 and n-2
        return fib(n - 1) + fib(n - 2)