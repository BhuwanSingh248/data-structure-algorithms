class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10**6
        msf = 0
        for i in nums:
            msf = max(msf+i, i)
            max_sum = max(msf, max_sum)
        return max_sum