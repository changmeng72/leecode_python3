class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = [start+(i<<1) for i in range(n)]
        from functools import reduce
        return reduce(lambda v,e : v^e ,r)