class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msf = nums[0]
        mtl = nums[0]
        for i in nums[1:]:
            mtl = max(i, mtl+i)
            msf= max(mtl, msf)
        return msf            