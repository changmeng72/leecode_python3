class Solution:
    def toLowerCase(self, s: str) -> str:
        r = list(s)
        for i in range(len(s)):
            if 'A'<= r[i] <= 'Z':
                r[i] = chr(ord(r[i])+32)
        return ''.join(r)