class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in nums:
            if curr < 0:
                return False
            if i > curr:
                curr = i
            curr -= 1
        return True
