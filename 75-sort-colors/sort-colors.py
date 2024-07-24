class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        once, zeroes, n = 0, 0, len(nums)

        for i in nums:
            if i == 0:
                zeroes += 1
            if i ==1 :
                once+=1


        for i in range(zeroes):
            nums[i] = 0
        
        for i in range(zeroes, zeroes+once):
            nums[i] = 1
        
        for i in range(zeroes+once, n):
            nums[i] = 2