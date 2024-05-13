class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        ans = n * (1 << (m-1))

        for j in range(1,m):
            cnt = 0 
            for i in range(n):
                cnt += grid[i][j]^1 if grid[i][0] == 0 else grid[i][j]
            
            if cnt < n - cnt:
                ans += (n-cnt) * (1 << (m-1-j))
            else:
                ans += (cnt) * (1 << (m-1-j))
        return ans 