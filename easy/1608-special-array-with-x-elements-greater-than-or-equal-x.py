class Solution:
    def specialArray(self, nums: List[int]) -> int:
        res = -1
        nums.sort()
        
        l = len(nums) 
        c = 0;
        
        for i in range(l-1,-1,-1):
            c += 1
            if nums[i]>=c:
                continue
            else:
                c = c -1
                if(nums[i]==c):
                    return -1
                else:
                    return c
        return c if c>0 else -1
            
                    
            
        
        
        
        
        """
        for i in range(l):
            if (l-i) <= nums[i]:
                if i>1 and nums[i-1] >= (l-i):
                    continue
                res = l-i
                break        
       
        return res
        """