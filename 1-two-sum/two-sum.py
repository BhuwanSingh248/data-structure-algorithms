class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i,j in enumerate(nums):
            required = target-j
            if j in nums_map:
                return [nums_map.get(j), i]
            nums_map[required] = i

        