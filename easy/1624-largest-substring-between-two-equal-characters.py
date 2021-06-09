class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_dict = {}
        max = 0
        for i in range(len(s)):
            t = char_dict.get(s[i],-1)
            if t==-1:
                char_dict[s[i]] = i
            else:
                if i-t>max:
                    max = i-t
        return max-1