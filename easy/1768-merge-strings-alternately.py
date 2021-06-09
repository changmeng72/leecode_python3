class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        c =  ''.join(''.join(x) for x in zip(word1,word2))
        if(len(word1)>len(word2)):
            return c + word1[len(word2):]
        if(len(word2)>len(word1)):
            return c + word2[len(word1):]
        return c