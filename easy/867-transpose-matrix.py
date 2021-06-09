class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        
        for i in range(len(matrix[0])):
            t = []
            for j in range(len(matrix)):
                t.append(matrix[j][i])
            res.append(t)
        return res
                