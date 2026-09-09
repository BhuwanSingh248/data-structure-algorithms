class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current_sum = 0
        minimum_size = float('inf')

        for end in range(len(nums)):
            current_sum += nums[end]
            while current_sum >= target:
                minimum_size = min(minimum_size, end - start + 1)
                current_sum -= nums[start]
                start += 1
        return minimum_size if minimum_size != float('inf') else 0