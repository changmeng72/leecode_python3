class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse = True)
        r = 0
        remaining = truckSize
        for boxType in boxTypes:
            b = min(remaining,boxType[0])
            r += b * boxType[1]
            remaining -= b
            if remaining==0:
                break
        return r
            