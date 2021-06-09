class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = [(i, sum(mat[i])) for i in range(len(mat))]
        d.sort(key=lambda x: x[1]*len(mat) + x[0])
        return [d[i][0] for i in range(k)]