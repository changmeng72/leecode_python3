class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 1
        for c in s+t:
            res ^= ord(c)
        
        return chr(res ^ 1)
        
        """
        char_dict = {}
        ans = None
        for c in s:
            char_dict[c] = char_dict.get(c,0) + 1
        
        for c in t:
            num = char_dict.get(c,0)
            if num==0:
                ans = c
                break
            else:
                char_dict[c] = num -1
        return ans
        """ 
                
            
        