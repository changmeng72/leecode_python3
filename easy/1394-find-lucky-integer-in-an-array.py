class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = {}
        
        for i in arr:
            dic[i] = dic.get(i,0) + 1
        m = -1
        
        for k,v in dic.items():
            if k==v:
                if k>m:
                    m = k
        return m
        
        
        """
        return max( [x[0] for x in filter(lambda x: x[0]==x[1], Counter(arr).items())],default=-1)
        """