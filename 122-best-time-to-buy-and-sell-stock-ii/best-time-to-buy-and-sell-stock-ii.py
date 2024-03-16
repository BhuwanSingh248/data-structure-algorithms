class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        # bruteforce 
        def helper(i, buy):
            if i >= len(prices):
                return 0
            if buy:
                profit = max(-prices[i] + helper(i+1, 0), helper(i+1, 1))
            else:
                profit = max(prices[i] + helper(i+1, 1), helper(i+1, 0))
            return profit

        #  using top down dp
        def helperDP(i, buy, dp):
            if i >= len(prices):
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            if buy:
                profit = max(-prices[i] + helperDP(i+1, 0, dp), helperDP(i+1, 1, dp))
            else:
                profit = max(prices[i] + helperDP(i+1, 1, dp), helperDP(i+1, 0, dp))
            
            dp[i][buy] = profit
            return profit

        # using bottom up dp
        def bottomUP():
            dp = [[0] * 2 for _ in range(len(prices) + 1)]
            for i in range(len(prices)-1, -1, -1):
                dp[i][0] = max(prices[i] + dp[i+1][1], dp[i+1][0])
                dp[i][1] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
            return dp[0][1]
        return bottomUP()

        # return helper(0, 1)
        # dp = [[-1] * 2 for _ in prices]
        # ans = helperDP(0, 1,dp)
        # return ans