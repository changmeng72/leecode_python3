class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minNum,maxNum = min(nums),max(nums)
        if maxNum-minNum>=2*k:
            return maxNum-minNum-2*k
        else:
            return 0