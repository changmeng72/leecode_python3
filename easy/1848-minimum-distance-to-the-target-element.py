class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = math.inf
        
        
        
        for i in range(len(nums)):            
            if nums[i]==target:
                diff =  abs(i-start)
                if diff < ans:
                    ans = diff
        return ans