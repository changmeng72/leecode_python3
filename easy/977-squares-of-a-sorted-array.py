class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        r = [0 for x in nums]
        left = 0
        right = len(nums)-1
        last = right
        
        while(last>=0):
            if abs(nums[left]) >(nums[right]) :
                r[last] = nums[left] * nums[left]
                left += 1 
            else:
                r[last] = nums[right] * nums[right]
                right -= 1
            last -= 1
                
        return r                           
        
        
        """
        r = [x*x for x in nums]
        if(nums[0]<0) :
            r.sort()
        return r
        """