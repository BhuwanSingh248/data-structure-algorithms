class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            pft = i - buy
            if pft < 0:
                buy = i
            
            profit = max(profit, pft)
        
        return profit