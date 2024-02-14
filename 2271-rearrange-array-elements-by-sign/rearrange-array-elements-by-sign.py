class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr=[0] * len(nums)
        p_i = 0
        n_i = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                arr[p_i] = nums[i]
                p_i += 2
            if nums[i] < 0:
                arr[n_i] = nums[i]
                n_i += 2
        return arr
            