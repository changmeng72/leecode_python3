class Solution:
    def numberOfMatches(self, n: int) -> int:
        r = 0
        while n>1:
            if(n%2):
                n = ((n-1)>>1) +1
                r = r + n - 1 
            else:
                n = n>>1
                r = r + n 
        return r
         
"""
class Solution:
    def numberOfMatches(self, n: int) -> int:   
        r  =n -1
        return r
"""