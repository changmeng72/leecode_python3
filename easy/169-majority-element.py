       
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        cur = nums[0]
        count = 1
        
        for i in range(1,len(nums)):
            if cur:
                if cur==nums[i]:
                    count += 1
                else:
                    count -= 1
                    if count==0:
                        cur = None
            else:
                cur = nums[i]
                count = 1
        return cur
            