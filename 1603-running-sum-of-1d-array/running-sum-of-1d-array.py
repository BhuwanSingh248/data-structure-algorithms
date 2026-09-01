class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = 0
        for i,j in enumerate(nums):
            nums[i] = temp+j
            temp += j
        return nums