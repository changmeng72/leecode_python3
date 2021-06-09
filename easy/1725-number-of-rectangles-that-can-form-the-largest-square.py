class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return sorted(Counter([min(l) for l in rectangles]).items(),reverse=True)[0][1]
