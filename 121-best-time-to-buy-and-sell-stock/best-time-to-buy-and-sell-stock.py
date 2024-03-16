class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in prices[1:]:
            sell = max(sell, i-buy)
            buy = min(buy, i)
        return sell