class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
        # If out of bounds or cell is empty, return 0
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return 0
            
            # Collect the gold in the current cell
            gold = grid[x][y]
            # Mark the cell as visited by setting it to 0
            grid[x][y] = 0
            
            # Explore all four possible directions
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            
            # Backtrack: restore the gold amount in the cell
            grid[x][y] = gold
            
            # Return the collected gold plus the maximum gold from further exploration
            return gold + max_gold

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_gold = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    max_gold = max(max_gold, dfs(i, j))
        
        return max_gold