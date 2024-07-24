class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10**5
        max_so_far = 0

        for i in nums:
            if max_so_far >=0:
                max_so_far += i
            else:
                max_so_far = i
            
            if max_so_far > max_sum:
                max_sum = max_so_far
        return max_sum