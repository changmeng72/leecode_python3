class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a==b else max(len(a),len(b)) if len(a)!=len(b) else len(a)
        