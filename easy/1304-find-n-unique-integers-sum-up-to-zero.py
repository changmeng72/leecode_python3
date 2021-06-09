class Solution:
    def sumZero(self, n: int) -> List[int]:         
        r = [i for i in range(1,n)]
        r.append(0-sum(r))
        return r 