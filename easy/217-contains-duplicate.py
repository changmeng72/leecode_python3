class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False
            
        
        
"""        
        num_dict = {}
        for num in nums:
            if num_dict.get(num,0)==0:
                num_dict[num] = 1
            else:
                return True
        return False
 """       
         
        
        
        ## return len(set(nums)) != len(nums)
        