class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c,0) + 1
        
        for c in t:
            k = s_dict.get(c,-1)
            if(k<1):
                return False
            s_dict[c] = k-1
        return True
        