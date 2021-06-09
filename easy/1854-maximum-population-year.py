class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        minr = min([ele[0] for ele in logs])
        maxr = max([ele[1] for ele in logs])
        m = 0
        y = minr
        for i in range(minr,maxr):
            count = 0
            for p in logs:
                if p[0] <=i and p[1]>i:
                    count += 1
            if count> m:
                m = count
                y  = i
       
        return y
            