class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = nums.copy()
        nums1.sort()         
        import collections
        d = {}
         
        for i in range(len(nums1)):
            if(nums1[i] not in d.keys()):
                d[nums1[i]] = i
        for i in range(len(nums1)):
            nums[i] = d[nums[i]]
        return nums   