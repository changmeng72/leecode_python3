class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr) * 5 //100
        return sum(arr[n:-n])/(len(arr)-(n<<1))