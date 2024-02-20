class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        tot = sum(nums)
        tot_n = count + (count * (count -1)) // 2 
        return tot_n - tot