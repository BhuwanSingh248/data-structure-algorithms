class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s,b = 1, 0
        buy = prices[b]
        profit = 0
        while s < len(prices):
            profit = max(profit, (prices[s] - buy))
            b += 1
            buy = min(buy, prices[b])
            s += 1
        return profit if profit>0 else 0