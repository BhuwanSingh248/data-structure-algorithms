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
        

        # bottomup dp with space optimization
        def bottomUpSpaceOptimized():
            # values depends on next value's buy or sell so will keep 4 vars
            # dp[i+1][1] --> next_buy
            # dp[i+1][0] --> next sell
            # dp[i][1] --> current_buy
            # dp[i][0] --> current_sell

            next_buy, next_sell, current_buy, current_sell = 0,0,0,0

            for i in range(len(prices)-1, -1, -1):
                current_buy = max(-prices[i] + next_sell, next_buy)
                current_sell = max(prices[i] + next_buy, next_sell)
                next_buy = current_buy
                next_sell = current_sell
            
            return next_buy

        # return helper(0, 1)
        # dp = [[-1] * 2 for _ in prices]
        # ans = helperDP(0, 1,dp)
        # return ans
        # return bottomUP()
        def btbss2():
            i = 1
            n = len(prices)
            profit = 0
            while i < n:
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
                i+=1
            return profit
        return btbss2()