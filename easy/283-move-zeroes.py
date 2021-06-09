class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.        
        
        """
        zerop = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zerop],nums[i] = nums[i],nums[zerop]
                zerop += 1
        
        
        
        """
        zerop = -1
        onep = None
        while True:
            flag = True
            for i in range(zerop+1,len(nums)):
                if nums[i]==0:
                    zerop = i
                    flag = False
                    break
            if flag:
                return
            flag = True
            
            for i in range(zerop+1,len(nums)):
                if nums[i]!=0:
                    onep = i
                    flag = False
                    break
            if flag:
                return
        
            nums[zerop],nums[onep] =  nums[onep],nums[zerop]
        
            """
            
                