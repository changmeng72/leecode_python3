class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([x for x in nums if x & 1==0])
        res = []
        for q in queries:
            if nums[q[1]] & 1 ==0:
                even_sum -=  nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] & 1 ==0:
                even_sum +=  nums[q[1]]
            
            res.append(even_sum)
                
                
        return res