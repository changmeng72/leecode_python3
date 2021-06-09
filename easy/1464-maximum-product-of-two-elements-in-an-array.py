class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        f,s = nums[0],nums[1]
        if f<s:
            f,s = s,f
        
        for i in range(2,len(nums)):
            if nums[i] >=f:
                f,s = nums[i],f
            elif nums[i] >s:
                s = nums[i]
        return f*s-f-s+1
"""
        nums.sort()
        return (nums[len(nums)-1]-1)*(nums[len(nums)-2]-1)
"""