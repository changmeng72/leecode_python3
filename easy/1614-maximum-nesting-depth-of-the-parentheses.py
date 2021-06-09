class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        i = 0
        for c in s:
            if c=='(':
                i += 1
                if(i>m):
                    m = i
            elif c==')':
                i -= 1
        return m
        