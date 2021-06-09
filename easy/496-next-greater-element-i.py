class Solution:
    def nextGreaterElement(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        d={}
        i = 0
        for elem in arr2:
            d[elem] = i
            i += 1
        for v in  arr1 :
            flag = True
            for j in range(d[v]+1,len(arr2)):
                if arr2[j] > v:
                    res.append(arr2[j])
                    flag = False
                    break
            if flag:
                res.append(-1)
        return res
            