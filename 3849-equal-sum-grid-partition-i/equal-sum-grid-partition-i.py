class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = 0

        for i in grid:
            total_sum += sum(i)

        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2 

        # check vertically 
        for i in grid:
            target -= sum(i)
            if target == 0:
                return True
            
            if target < 0:
                break
        target = total_sum // 2 
        # check horizntal split
        for i in range(len(grid[0])):
            temp = 0
            for j in range(len(grid)):
                temp += grid[j][i]
            target -= temp
            print(' ---> ', target)
            if target == 0:
                return True
            
            if target < 0:
                break

        return False