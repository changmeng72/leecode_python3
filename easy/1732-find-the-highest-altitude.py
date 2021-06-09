class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = gain[0] if gain[0]>0 else 0
        for i in range(1,len(gain)):
            gain[i] += gain[i-1]
            if gain[i] > m:
                m  =gain[i]
        return m