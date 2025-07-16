class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -10 ** 6 
        max_so_far = 0
        for i in nums:
            max_so_far = max(i, max_so_far + i)
            max_val = max(max_val, max_so_far)
        return max_val