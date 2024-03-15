class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        is_zero = 0
        is_negative = 0
        for i in nums:
            if i == 0:
                is_zero += 1
            else:
                prod *= i
        for i in range(len(nums)):
            if nums[i] == 0:
                if is_zero < 2:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                if is_zero:
                    nums[i] = 0
                else:
                    nums[i] = prod // nums[i]
        return nums
