class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dp = {}
        max_element= 0 
        val = 0
        for i in range(len(nums)):
            val += 1 if nums[i] else -1

            if val == 0:
                max_element = i + 1  
            
            if val in dp:
                max_element = max(max_element, i - dp[val])
            else:
                dp[val] = i
        return max_element