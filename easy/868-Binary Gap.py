class Solution:
    def binaryGap(self, n: int) -> int:
        if n==0:
            return 0
        c,m = 0,0
        
        while n&1==0:
            n>>=1
        n>>=1    
        while n>0:
            if n&1==1:
                if c+1>m:
                    m=c+1
                c = 0
            else:
                c += 1
            n >>= 1
        return m
            
            
        