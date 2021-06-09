class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        
        for i in range(1,n+1):
            if i & 1:
                res[i] = res[i//2] + 1
            else:
                res[i] = res[i//2]
        return res
        
        """
        dic = {}
        r = []
        for i in range(n+1):
            cn = i
            bn = 0
            while cn!=0:
                bn += cn%2
                cn = cn>>1
                t = dic.get(cn,0)
                if t!=0:
                    bn += t
                    break
            dic[i] = bn
            r.append(bn) 
        return r
        """        
                