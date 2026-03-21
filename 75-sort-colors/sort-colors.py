class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        once = 0
        twos = 0
        zeros = 0

        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                once += 1
            else:
                twos += 1

        for i in range(len(nums)):
            if zeros:
                nums[i] = 0
                zeros -= 1

            elif once:
                nums[i] = 1
                once -= 1
            else:
                nums[i] =2
                