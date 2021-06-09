class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        k = n
        r = 0
        for i in range(m):
            for j in range(k):
                if(grid[i][j]<0):                   
                    r += (k-j)*(m-i) 
                    k = j
                    break
            if k==0:
                break
        return r