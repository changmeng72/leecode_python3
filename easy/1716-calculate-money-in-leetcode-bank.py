class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        firstweek = sum([i for i in range(1,8)])
        s = sum([i for i in range(1,weeks)]) * 7 + firstweek * (weeks)
        remains = n % 7
        
        s += sum([i for i in range(1,remains+1)]) + remains * weeks
        return s