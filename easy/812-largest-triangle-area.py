class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ans = 0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    a= abs((points[i][0]*(points[j][1]-points[k][1])+
                        points[j][0]*(points[k][1]-points[i][1])+
                        points[k][0]*(points[i][1]-points[j][1]))/2)
                    if a > ans:
                        ans = a
        return ans
		
		
		
"""
 a = abs(x1(y2-y3)+x2(y3-y1) + x3(y1-y2))/2
"""
