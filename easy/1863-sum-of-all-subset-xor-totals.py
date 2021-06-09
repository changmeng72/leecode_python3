class Solution:
    def subset(self,nums: List[int])->List[int]:
        if(len(nums)<2):
            return nums
        t = self.subset(nums[1:])
        s = [nums[0]]
        for i in range(len(t)):
            s.append(nums[0] ^ t[i])
            s.append(t[i]) 
        return s
    
    def subsetXORSum(self, nums: List[int]) -> int:        
        s = self.subset(nums)        
        return sum(s)