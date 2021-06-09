class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return  [x[0] for x in sorted(Counter(s1.split(' ') +  s2.split(' ')).items(),key=lambda x: x[1]) if x[1]==1]