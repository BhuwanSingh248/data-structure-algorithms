class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
    
        # Step 1: Calculate minimum distance from each cell to any thief using BFS
        distance = [[float('inf')] * n for _ in range(n)]
        queue = deque()

        # Initialize the BFS with all thief positions
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    distance[r][c] = 0
                    queue.append((r, c))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == float('inf'):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        # Step 2: Use a max-heap to find the path maximizing the minimum safeness factor
        max_heap = [(-distance[0][0], 0, 0)]
        max_safeness = [[-float('inf')] * n for _ in range(n)]
        max_safeness[0][0] = distance[0][0]
        
        while max_heap:
            curr_safeness, r, c = heapq.heappop(max_heap)
            curr_safeness = -curr_safeness
            
            if r == n - 1 and c == n - 1:
                return curr_safeness
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safeness = min(curr_safeness, distance[nr][nc])
                    if new_safeness > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safeness
                        heapq.heappush(max_heap, (-new_safeness, nr, nc))
        
        return 0