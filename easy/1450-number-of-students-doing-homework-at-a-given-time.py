class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                count += 1
        return count
    
    
    """d = {}
        for i in range(len(startTime)):
            for t in range(startTime[i],endTime[i]+1):
                if t in d.keys():
                    d[t] += 1
                else:
                    d[t] = 1
        return  d.get(queryTime,0)
    """        