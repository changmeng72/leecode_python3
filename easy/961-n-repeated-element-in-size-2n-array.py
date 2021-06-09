
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-2,2):
            if(nums[i]==nums[i+1]):
                return nums[i]
        temp = nums[len(nums)-4: len(nums)]        
        temp.sort()
        for i in range(3):
            if temp[i]==temp[i+1]:
                return temp[i]
        