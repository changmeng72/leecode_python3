class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums)<2:
            return True
        flag = 0
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                if flag == 0:
                    flag = 1
                elif flag==-1:
                    return False
            elif(nums[i]<nums[i-1]):
                if flag == 0:
                    flag = -1
                elif flag==1:
                    return False
        return True