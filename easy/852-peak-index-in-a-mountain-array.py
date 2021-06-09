class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo,hi = 0,len(arr)-1
        
        while lo<hi:
            mi = (lo+hi)//2
            if arr[mi]<arr[mi+1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
        
        
        """  
        def searchMountain(baseIndex,arr):
            
            n = len(arr)
            if(n==3):
                return baseIndex+1
            half = (len(arr)//2)
            if(arr[half]>arr[half+1] ): 
                if arr[half]>arr[half-1]:
                    return baseIndex + half
                else:
                    return searchMountain(baseIndex, arr[:half+1])
            else:
                return searchMountain(baseIndex+half, arr[ half:])
        return searchMountain(0,arr)
        
       
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return i
        return arr[len(arr)-1]
        """