class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        r = [0]*len(s)
        index = [i for i in range(len(s)) if s[i]==c[0]]
        start = -10001
        n = 0
        end = index[n]
        
        for i in range(len(s)):
            if(i<end):
                r[i]=(min(abs(i-start),abs(i-end)))
            else:
                start = end
                if(n==len(index)-1) :
                    end = 20001
                else:
                    end = index[n+1]
                n += 1
        return r
                
                            