class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dict = {}
            for i,j in enumerate(nums):
                val = target-j
                if val in dict:
                    return [dict[val], i]
                elif j not in dict:
                    dict[j] = i
            return []