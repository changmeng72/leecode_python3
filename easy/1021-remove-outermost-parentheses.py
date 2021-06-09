class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r =[]
        start = 0
        count = 1
        for i in range(1,len(s)):
            if(s[i]=='('):
                count += 1
            else:
                count -=1
                if(count==0):
                    r.append(s[start+1:i])
                    start = i+1
        return ''.join(r)