class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = []
        for row in range(len(matrix)):
            m = min(matrix[row])
            i = matrix[row].index(m)
            flag = True
            for k in range(len(matrix)):
                if matrix[k][i]>m:
                    flag = False
                    break
            if flag==True:
                r.append(m)
        return r
                    
                