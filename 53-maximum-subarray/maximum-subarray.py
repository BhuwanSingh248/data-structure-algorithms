class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = 0
        max_sum =  -float('inf')

        for i in nums:
            max_so_far = max(i, max_so_far + i)
            max_sum = max(max_so_far, max_sum)

        return max_sum