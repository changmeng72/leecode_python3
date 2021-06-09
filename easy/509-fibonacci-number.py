class Solution:
    def fib(self, n: int) -> int:
        res = [0,1]        
        for i in range(2,n+1):
            res[i%2] = res[0] + res[1]
        return res[n%2]
        
        
        
        """
        if n==0:
            return 0
        ns2 = 0
        ns1 = 1
        for i in range(2,n+1):
            t = ns1
            ns1 = ns1 + ns2
            ns2 = t
        return ns1
            
        """