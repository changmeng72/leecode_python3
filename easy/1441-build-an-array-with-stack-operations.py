class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        r = []
        s = 1
        for n in target:
            for i in range(s,n):
                r.append('Push')
                r.append('Pop')
            r.append('Push')
            s = n+1
        return r
