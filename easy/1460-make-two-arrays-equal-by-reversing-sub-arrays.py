class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        bucket = [0 ] *1001
        for i in target:
            bucket[i] += 1
        for i in arr:
            bucket[i] -= 1
        for i in bucket:
            if i!=0:
                return False
        return True
            
        """
        d = {}
        for i in target:
            d[i] = d.get(i,0) + 1
        for i in arr:
            d[i] = d.get(i,0) -1
            if(d[i] < 0):
                return False
        return sum(d.values())==0
      """  