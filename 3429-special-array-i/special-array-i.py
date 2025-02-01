class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        
        i,j = 0,1
        while(j <len(nums)):
            if nums[i]%2 == nums[j] %2:
                return False
            i,j = j, j+1
        return True
            