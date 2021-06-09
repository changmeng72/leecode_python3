class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp=[0 for i in range(n+1)]
        
        for i in range(1,n+1):
            b = i//10
            dp[i] = dp[b] + (i%10)
        
        c = Counter(dp[1:])
        
        t = sorted(c.items(),key=lambda x: x[1],reverse=True)
        n = t[0][1]
        
        return len([x for x in t if x[1]==n])
        
        
        """ 
        def sumdigit(m):
            s = 0
            while m>0:
                s += m%10
                m //= 10
            return s
        
        d = {}
        for i in range(1,n+1):
            k = sumdigit(i)
            d[k] = d.get(k,0) + 1
        v = d.items()
        
        t = sorted(v,key=lambda x: x[1], reverse=True)
        
        n = t[0][1]
        
        return len([x for x in t if x[1]==n])
       """     
        