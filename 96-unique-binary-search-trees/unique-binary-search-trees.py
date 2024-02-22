class Solution:
    def __init__(self):
        self.dp = None 
    def numTrees(self, n: int) -> int:
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