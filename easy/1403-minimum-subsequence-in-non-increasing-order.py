class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
       
        s1 = 0
        s = sum(nums)
        i = 0
        while s>=s1:
            s1 += nums[-1-i]
            s  -= nums[-1-i]
            i  += 1
        return nums[-1: -1-i:-1]