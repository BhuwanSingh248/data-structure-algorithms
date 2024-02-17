class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def solve(index, bricks, ladders, dp = {}):
            if index == len(heights):
                return 0
            key = f'{index}*{bricks}*{ladders}'
            if key in dp:
                return dp[key]

            using_ladder = 0
            using_brick = 0
            without_any = 0
            diff = heights[index] - heights[index-1]
            if diff > 0:
                if (bricks - diff) >= 0:
                    using_brick = 1 + solve(index + 1, bricks - diff, ladders, dp)
                
                if ladders > 0 :
                    using_ladder = 1 + solve(index+1, bricks, ladders - 1, dp)
            else:
                without_any = 1 + solve(index+1, bricks, ladders, dp)
            ans = max(using_brick, using_ladder, without_any)
            dp[key]= ans
            return ans
        # raising TLE
        # using min heap

        arr = []
        for i in range(len(heights) - 1):
            jump = heights[i+1] -  heights[i]
            if jump > 0:
                heapq.heappush(arr, jump)
            if len(arr) > ladders :
                bricks -= heapq.heappop(arr)
            
            if bricks < 0:
                return i
        return len(heights) -1

