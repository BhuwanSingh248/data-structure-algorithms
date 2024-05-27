class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(max(nums)+1):
            count = 0
            for j in nums:
                if j >= i:
                    count += 1
            if count == i:
                return i
        else:
            return -1