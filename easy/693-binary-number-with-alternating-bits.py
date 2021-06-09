class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur = n & 1
        while n>0:
            n >>= 1
            if(n&1 == cur):
                return False
            cur = n&1
        return True
            