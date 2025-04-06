class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}

        def find_divisible_subset(index):
            if index == len(nums):
                return []

            if index in memo:
                return memo[index]

            longest_subset = []
            for i in range(index + 1, len(nums)):
                if nums[i] % nums[index] == 0:
                    subset = [nums[i]] + find_divisible_subset(i)
                    if len(subset) > len(longest_subset):
                        longest_subset = subset

            memo[index] = longest_subset
            return longest_subset

        max_subset = []
        for i in range(len(nums)):
            subset = [nums[i]] + find_divisible_subset(i)
            if len(subset) > len(max_subset):
                max_subset = subset

        return max_subset
        