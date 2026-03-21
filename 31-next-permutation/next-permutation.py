class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        end = len(nums)-1
        while end > 0:
            if nums[end-1] < nums[end]:
                index = end-1
                break
            end -= 1
        
        if index == -1:
            nums.sort()
            return 
        nn = index + 1
        for i in range(index+1, len(nums)):
            if nums[i] > nums[index] and nums[i] < nums[nn]:
                nn = i
        nums[index],nums[nn] = nums[nn], nums[index]
        for i, j in enumerate(sorted(nums[index+1:]), index+1):  ## we can directly sort the array though
            nums[i] = j
        
