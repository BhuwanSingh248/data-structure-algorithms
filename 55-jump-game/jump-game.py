class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr = [False] * len(nums)
        arr[-1] = True
        for i in range(len(nums)-2, -1, -1):
            temp = i + nums[i]
            if i+nums[i] > len(nums):
                arr[i] = any(arr[i:len(nums)])
            else:
                arr[i] = any(arr[i: i+nums[i]+1])
    
        return arr[0] 

    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in nums:
            if curr < 0:
                return False
            if i > curr:
                curr = i
            curr -= 1
        return True



