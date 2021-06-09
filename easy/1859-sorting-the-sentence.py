class Solution:
    def sortSentence(self, s: str) -> str:
        str_lst = s.split()
        r = [None for i in range(len(str_lst))]
        for subs in str_lst:
            r[int(subs[-1])-1] = subs[:-1]
        return " ".join(r)
        
        
"""
class Solution:
    def sortSentence(self, s: str) -> str:
        return ' '.join([i[:-1] for i in sorted(s.split(), key=lambda x: x[-1])])
"""