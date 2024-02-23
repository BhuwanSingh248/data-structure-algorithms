class Solution:
    def numTrees(self, n: int) -> int:
        def helper(num, dp):
            ans = 0
            if num <= 1:
                return 1
            
            if dp[num] != -1:
                return dp[num]

            for i in range(1, num+1):
                ans += helper(i-1, dp) * helper(num-i, dp)
            dp[num] = ans
            return ans 
        dp = [-1] * (n+1)
        return helper(n, dp) 

