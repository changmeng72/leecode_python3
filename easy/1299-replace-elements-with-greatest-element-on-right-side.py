class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            t = arr[i]
            arr[i] = m
            if(m<t):
                m = t
        arr[len(arr)-1] = -1;
        return arr
            