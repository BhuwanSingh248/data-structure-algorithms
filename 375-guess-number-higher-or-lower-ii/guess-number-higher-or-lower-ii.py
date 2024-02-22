class Solution:
    def getMoneyAmount(self, n: int) -> int:
        max_int = n * (n)
        def solver(start:int, end: int) -> int : 
            if start >= end:
                return 0
            maxi = max_int
            for i in range(start, end):
                maxi = min(maxi, i +  max(solver(start, i-1), solver(i+1, end)))
            return maxi

        def solverMem(start:int, end:int , dp:List[List[int]]):
            if start>= end:
                return 0
            maxi = max_int

            if dp[start][end] != -1:
                return dp[start][end]

            for i in range(start, end):
                maxi = min(maxi, i + max(solverMem(start, i-1, dp), solverMem(i+1, end, dp)))

            dp[start][end] = maxi
            return maxi

        dp = [[-1] * (n+1) for _ in range(n+1)]
        return solverMem(1, n, dp) 

