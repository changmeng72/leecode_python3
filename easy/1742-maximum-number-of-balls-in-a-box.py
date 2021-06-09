class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_digit(num):
            r = 0
            while num>0:
                r += num %10
                num //=10
            return r
        d = {}
        for num in range(lowLimit,highLimit+1):
            t = sum_digit(num)
            d[t] = d.get(t,0) + 1
        return max(d.values())