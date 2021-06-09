class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        q = deque([[rCenter,cCenter]])
        res = [[rCenter,cCenter]]
        visited = [[0 for i in range(cols) ] for j in range(rows)]
        visited[rCenter][cCenter] = 1
        
        while q:
            c = q.popleft()
            for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0<=(c[0]+x)<rows and  0<=(c[1]+y)<cols :
                    if(visited[c[0] + x][c[1]+y]==0):
                        res.append([c[0] + x,c[1]+y])
                        visited[c[0] + x][c[1]+y] = 1
                        q.append([c[0] + x,c[1]+y])
        return res
                        
        
        
        
"""   

        l = []
        for r in range(rows):
            for c in range(cols):
                l.append(([r,c],abs(r-rCenter) + abs(c-cCenter)))
        l.sort(key = lambda x:x[1])
        return [x[0] for x in l]
""" 