class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l<r:
            while(l<(len(nums)) and nums[l] %2 == 0):
                l += 1
            while r>0 and nums[r] %2 == 1:
                r -= 1
            if(l<r ):
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        return nums