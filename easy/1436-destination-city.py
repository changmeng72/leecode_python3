
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for c in paths:
            s.add(c[0])
        for c in paths:
            if c[1] not in s:
                return c[1]