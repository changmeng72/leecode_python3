class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        curArray = arr.copy()        
        r = sum(curArray)        
        n = len(arr)-2
        j=0
        while n > 0:
            for i in range(n):
                curArray[i] = curArray[i] + arr[i+j+1] +arr[i+j+2]           
            r = r+ sum(curArray[:n]) 
            n = n -2
            j = j+2
        return r