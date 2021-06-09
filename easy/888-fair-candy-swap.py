class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        
        diff = (aliceSum - bobSum)/2
        
        bob_dict = {}
        for i in range(len(bobSizes)):
            bob_dict[bobSizes[i]] = i
        
        for i in range(len(aliceSizes)):
            k = bob_dict.get(aliceSizes[i]-diff,-1)
            if k!=-1:
                return [aliceSizes[i],bobSizes[k]]
        return [0,0]
        