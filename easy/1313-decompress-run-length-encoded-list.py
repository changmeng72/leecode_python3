class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
         r = []
        for i in range(len(nums)):
            if(i%2)==0:
                for j in range(nums[i]):
                    r.append(nums[i+1])
        return r
       
        