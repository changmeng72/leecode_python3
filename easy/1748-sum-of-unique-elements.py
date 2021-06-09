class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l = sorted(Counter(nums).items(),key=lambda x: x[1])
        r = 0
        for elem in l:
            if elem[1]==1:
                r += elem[0]
            else:
                break
        return r