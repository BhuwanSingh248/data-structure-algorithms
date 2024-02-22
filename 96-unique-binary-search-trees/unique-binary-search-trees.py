class Solution:
    def __init__(self):
        self.dp = None 
    def numTrees1(self, n: int) -> int:
        if not self.dp:
            self.dp = [-1] * (n+1)
        if n <= 1:
            return 1
        if self.dp[n] != -1:
            return self.dp[n]
        ans = 0
        for i in range(1,n+1):
            ans += self.numTrees(i-1) * self.numTrees(n-i)
        self.dp[n] = ans
        return ans 
    
    def numTrees(self, n):
        dp = [0] * (n+1)
        dp[0],dp[1] = 1, 1
        #  number of nodes
        for i in range(2, n+1):
            # assuing j as root node
            for j in range(1,n+1):
                dp[i] += dp[j-1] * dp[i - j]
        return dp[n]