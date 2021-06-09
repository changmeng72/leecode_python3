class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sortedNums =sorted( Counter(nums).items(),key = lambda x:x[1]*1000 - x[0])
        res = []
        for (k,v) in sortedNums:
            res.extend([k]*v)
        return res
        
		"""
		def frequencySort(self, nums: List[int]) -> List[int]:
        h, res = [], []
        C = collections.Counter(nums)
        for k, c in C.items():
            for _ in range(c):
                heappush(h, (c, -k))
        while h:
            res.append(-heappop(h)[1])
        return res
		"""