@lru_cache
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n  = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1

        for i in range(n):
            if abs(nums[i]) <= n and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1

        # flag = 0        
        for i in range(1, n+1):
            if nums[i-1] >= 0:
                # flag += 1 
                return i
        return n+1