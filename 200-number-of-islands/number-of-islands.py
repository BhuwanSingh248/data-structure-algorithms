class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        
        cols = len(grid[0])

        no_of_island = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.mark_current_island(grid, i, j, rows, cols)
                    no_of_island += 1
        return no_of_island
    
    def mark_current_island(self, grid, x, y, r, c):
        if x < 0 or x>=r or y  < 0 or y >= c or grid[x][y] != '1':
            return 
        
        grid[x][y] = '2'

        # call for all adjacent direction

        self.mark_current_island(grid, x+1, y, r, c) #down
        self.mark_current_island(grid, x, y+1, r, c) # right
        self.mark_current_island(grid, x-1, y, r, c) # top
        self.mark_current_island(grid, x, y-1, r, c) # left
    
