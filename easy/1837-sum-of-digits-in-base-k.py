class Solution:
    def sumBase(self, n: int, k: int) -> int:
        r = 0
        while n>0:
            r += n%k
            n = n//k
        return r
        