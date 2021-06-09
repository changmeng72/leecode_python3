class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        r = 0
        for i in range(len(grid)):
            r += max(grid[i])            
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    r += 1
        for j in range(len(grid[0])):
            r += max(grid[i][j] for i in range(len(grid)))
        return r
                    