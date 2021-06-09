class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = x^y
        r = 0
        while c != 0:
            r += (c & 1)
            c = c>>1
        return r
        