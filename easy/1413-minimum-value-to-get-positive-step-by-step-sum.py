class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        for num in nums:
            s += num
            if s<m:
                m = s
        if m<1:
            return 1-m
        else:
            return 1
        
        