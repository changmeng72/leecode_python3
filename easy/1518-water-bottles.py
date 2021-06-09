class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles;
        emptybottles = numBottles
        remains = 0
        
        while emptybottles>=numExchange:            
            numBottles  = emptybottles // numExchange
            res += numBottles
            emptybottles  = emptybottles%numExchange+  numBottles
        return res
            