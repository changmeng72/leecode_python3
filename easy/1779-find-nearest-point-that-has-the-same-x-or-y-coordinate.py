class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDistance = 10000
        
        res = -1
        
        for i in range(len(points)):
            if points[i][0]==x:
                d = abs(points[i][1]-y)
                if d< minDistance:
                    minDistance = d
                    res = i
             
            elif points[i][1]==y:
                d = abs(points[i][0]-x)
                if d< minDistance:
                    minDistance = d
                    res = i
        return res
                
        