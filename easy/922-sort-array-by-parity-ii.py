class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd,even = 1,0
        while odd<len(nums) and even<len(nums):
            while  odd<len(nums) and nums[odd] & 1 :
                odd += 2
            while  (even < len(nums) and (nums[even]  & 1)!=1 ):
                even += 2
            if  even<len(nums) and odd<len(nums) :
                nums[odd],nums[even] = nums[even],nums[odd] 
        return nums