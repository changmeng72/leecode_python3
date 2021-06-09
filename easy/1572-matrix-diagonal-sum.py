class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            s += mat[i][i] + mat[i][len(mat)-1-i]
        if len(mat)%2:
            s -=  mat[len(mat)//2][len(mat)//2]
        return s
"""
return sum(mat[i][i] + mat[len(mat)-i-1][i] for i in range(len(mat))) - (len(mat)%2) * (mat[len(mat)//2][len(mat)//2])
"""