def myPow(x, n):
    def cal_pow(x, n):
        if x == 0: # 0^n = 0
            return 0
        if n == 0: # x^0 = 1
            return 1

        res = cal_pow(x, n // 2) # divide n by 2
        res *= res # multiply the result by itself

        if n % 2 == 1: # if n is odd, then multiply the result by x
            return res * x
        else: # if n is even, then return the result
            return res

    ans = cal_pow(x, abs(n))
    if n < 0: # if n is negative, then return 1/ans
        return (1/ans)
    else:
        return ans