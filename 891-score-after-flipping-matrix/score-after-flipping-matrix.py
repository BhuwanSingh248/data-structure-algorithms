class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        ans = n * (1 << (m-1 -0))

        for j in range(1,m):
            colCount = 0 
            for i in range(n):
                colCount += grid[i][j]^1 if grid[i][0] == 0 else grid[i][j]
            
            if colCount < n - colCount:
                ans += (n-colCount) * (1 << (m-1-j))
            else:
                ans += (colCount) * (1 << (m-1-j))
        return ans 