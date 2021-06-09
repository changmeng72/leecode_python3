class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def bitsOf(n):
            r = 0
            while n!=0:
                r += n &1
                n = n>>1
            return r
        for i in range(len(arr)):
            arr[i] = (arr[i],bitsOf(arr[i]))
        arr.sort(key=lambda x: x[1])
        for i in range(len(arr)):
            arr[i] = arr[i][0]
        return arr
        