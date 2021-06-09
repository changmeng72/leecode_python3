class Solution:
    def checkIfPangram(self, sentence: str) -> bool:         
        d = dict(Counter("abcdefghijklmnopqrstuvwxyz"))         
        for c in sentence:
            d[c] = 0 
        return sum(d.values())==0
        
"""
if set("abcdefghijklmnopqrstuvwxyz") - set(sentence) == set():
            return True
        return False
"""

"""
return  len(set(sentence))==26 
"""