class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        top,front,left = 0,0,0
        rowSurface =[grid[i][0]+grid[i][len(grid[0])-1] for i in range(len(grid))]
        colSurface =[grid[0][i] + grid[len(grid)-1][i]  for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if(grid[i][j] > 0):
                    top += 1                
                if(i>0 and grid[i][j]!=grid[i-1][j]):
                    colSurface[j] += abs(grid[i][j]-grid[i-1][j])
                if(j>0 and grid[i][j-1]!=grid[i][j]):
                    rowSurface[i] += abs(grid[i][j]-grid[i][j-1])
        
                    
         
        return (top + top + sum(rowSurface) + sum(colSurface)) 
        