class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)-1):

            max_profit = max(prices[i+1:]) - prices[i]
            if max_profit > profit:
                profit = max_profit
        
        return profit
