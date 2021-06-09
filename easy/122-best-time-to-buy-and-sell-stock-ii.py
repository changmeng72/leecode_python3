class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        status = -1
        profits = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                if status == -1:
                    status = prices[i-1]
            elif prices[i] < prices[i-1]:
                if status > -1:
                    profits += prices[i-1]-status
                    status = -1
        if status>-1 and status < prices[len(prices)-1]:
            profits += prices[len(prices)-1] - status
        return profits
        