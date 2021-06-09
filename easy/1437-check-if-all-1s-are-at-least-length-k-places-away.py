class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        c = k
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                if c<k:
                    print(c,k)
                    return False
                c = 0
        return True
                
        """
        prev = 0-k-1
        for i in range(len(nums)):
            if nums[i]==1:
                if i-prev>=k+1:
                    prev = i
                else:
                    return False
            else:
                pass
        return True
                
        """