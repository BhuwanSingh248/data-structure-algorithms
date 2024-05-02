class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) -1

        while j > i:
            if nums[i] > 0:
                break
            if abs(nums[i]) == nums[j]:
                return nums[j]
            elif abs(nums[i]) > nums[j]:
                i += 1
            else:
                j -= 1
        
        return -1 
