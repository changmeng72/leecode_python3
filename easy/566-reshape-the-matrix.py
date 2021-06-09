class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        if r*c!=rows*cols:
            return mat
        total = r*c
        res = [[] for i in range(r)]
        for i in range(rows):
            row = i* cols
            for j in range(cols):
                k =  row  + j
                if(k>=total):
                    return res
                res[k//c].append(mat[i][j])
        return res
                