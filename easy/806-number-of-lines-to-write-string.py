class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result=[0,0]
        lineWidth = 0
        for c in s:
            i = ord(c)-ord('a')
            if(lineWidth + widths[i] <= 100):
                lineWidth += widths[i]
            else:
                result[0] += 1
                lineWidth = widths[i]
        result[0] += 1
        result[1] = lineWidth
        return result
                