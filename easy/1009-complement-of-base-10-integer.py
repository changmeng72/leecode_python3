class Solution:
    def bitwiseComplement(self, n: int) -> int:
        res,k = 0,0
        if n==0:
            return 1
        
        k = ~0
        
        while n&k:
            k <<= 1
        return ~k-n
""" 
        while n>0:
            if n&1 == 0:
                res += 1<<k
            k += 1
            n = n>>1
        return res
"""         
        
        
        