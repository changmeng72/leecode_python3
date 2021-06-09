class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)==0:
            return []
        listwithindex  = [[arr[i],i] for i in range(len(arr))]
        listwithindex.sort()
        rank = 1
        arr[listwithindex[0][1]] = rank
        for i in range(1,len(arr)):
            if listwithindex[i][0]==listwithindex[i-1][0]:
                arr[listwithindex[i][1]] = rank
            else:
                rank += 1
                arr[listwithindex[i][1]] = rank
        return arr