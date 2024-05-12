class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_grid = [[0] * (n - 2) for _ in range(n-2)]
        for i in range(n):
            if i+3 > n:
                break
            for j in range(n):
                if j + 3 > n:
                    break 

                max_grid[i][j] = max(map(max, [row[j:j+3] for row in grid[i:i+3]]))
        return max_grid  
            

