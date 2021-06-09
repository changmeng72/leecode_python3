class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        r = []
        mx = len(s)
        mn = 0
        for c in s:
            if c=='I':
                r.append(mn)
                mn += 1
            else:
                r.append(mx)
                mx -= 1
        r.append(mx)
        return r