class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            r = True
            while num!=0:
                num //=10
                r = not r
            count =  count + r    
        return count
 
"""
return sum(len(str(num)))%2==0 for num in nums)
"""