class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        allchars = set(s)
        ml = 0
        for i in range(len(s)):
            if s[i] in allchars and s[i].swapcase() in allchars:
                continue
            s1 = self.longestNiceSubstring(s[:i])  
            s2 = self.longestNiceSubstring(s[i+1:]) 
            if len(s2) > len(s1):
                return s2
            else:
                return s1
        return s