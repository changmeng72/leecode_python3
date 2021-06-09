class Solution:
    def maxScore(self, s: str) -> int:
        ones  = 0
        for c in s:
            if c=='1':
                ones += 1
        score = 1 + ones if s[0]== '0' else ones-1
        max_score = score
        for i in range(1,len(s)-1):
            if s[i]=='1':
                score -= 1
            else:
                score += 1
                if score > max_score:
                    max_score = score
        return max_score