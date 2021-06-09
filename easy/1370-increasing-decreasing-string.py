class Solution:
    def sortString(self, s: str) -> str:        
        c = []
        for t in sorted(Counter(s).items()):
            c.append(list(t))
        r = ''
        flag = True
        
        while flag:
            flag = False
            for e in c:
                if e[1]>0:
                    r += e[0]
                    flag = True
                    e[1] -= 1
            for i in range(len(c)-1,-1,-1):
                if c[i][1] > 0:
                    r += c[i][0]
                    c[i][1] -= 1
                    flag = True
        return r
        
"""
class Solution:
    def sortString(self, s: str) -> str:
        m={}
        for i in s:
            m[i]=m.get(i,0)+1
        ns=""
        keys=sorted(m.keys())
        while True:
            if len(ns)==len(s):
                return ns
            for i in keys+keys[::-1]:
                if m[i]>0:
                    ns+=i
                    m[i]=m[i]-1
"""