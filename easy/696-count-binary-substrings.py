class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ans,prev,cur = 0,0,1
        
        for i in range(1,len(s)):
            
            if s[i] != s[i-1]:
                prev,cur = cur,1
                ans += 1
            else:
                cur += 1
                if cur<=prev:
                    ans += 1
        return ans
            
            
            
    
    
    
    """       
        stack = []
        
        res = 0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                stack.append([i,i+1])
        res += len(stack)
        while stack:
            seg = stack.pop()            
            for i in range(1,seg[0]+1):            
                if seg[1]+i<len(s) and s[seg[0]-i]== s[seg[0]] and s[seg[1]+i]==s[seg[1]]:
                    res += 1
                else:
                    break
                 
        return res
                
    """            
    """Intuition and Algorithm

We can amend our Approach #1 to calculate the answer on the fly. Instead of storing groups, we will remember only prev = groups[-2] and cur = groups[-1]. Then, the answer is the sum of min(prev, cur) over each different final (prev, cur) we see."""       
        