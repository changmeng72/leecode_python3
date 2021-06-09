class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        colsum = [0 for i in range(len(mat[0]))]
        rowsum = [0 for i in range(len(mat))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rowsum[i] += mat[i][j]
                colsum[j] += mat[i][j]
        
        for i in range(len(mat)):
            if(rowsum[i]==1):
                for j in range(len(mat[0])):
                    if mat[i][j]==1:
                        result += 1 if colsum[j]==1 else 0
                        break
        return result
        
"""

        res = 0
        colflag = [True for i in range(len(mat[0]))]
        
        for r in range(len(mat)):
            flag = -1 
            rowflag = True
            for c in range(len(mat[0])):        
                if mat[r][c]==1:
                    if colflag[c]==False:
                        rowflag = False
                    if flag == -1:
                        flag = c                        
                    else:
                        rowflag = False
                        colflag[c] = False
                           
            if rowflag==False:
                colflag[flag] = False
                
                
       
        for c in range(len(mat[0])):
            if(colflag[c]):
                s = sum([mat[r][c] for  r in range(len(mat))])
                if s==1:
                    res += 1
        return res
                       

"""                        
            