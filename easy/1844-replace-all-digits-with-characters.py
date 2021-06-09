class Solution:
    def replaceDigits(self, s: str) -> str:
        r = [s[i] for i in range(len(s))]
        for i in range(1,len(s),2):            
            r[i] = chr(ord(r[i-1])+int(r[i]))
        return ''.join(r)
            