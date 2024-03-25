class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] < 0:
                arr.append(abs(nums[i]))
            else:
                nums[temp] = -nums[temp]
        return arr

