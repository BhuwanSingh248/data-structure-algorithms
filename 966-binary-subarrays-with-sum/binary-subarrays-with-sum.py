class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = {0:1}
        current_sum = 0
        ans = 0
        for i in nums:
            current_sum += i
            if current_sum - goal in count:
                ans += count[current_sum-goal]
            count[current_sum] = count.get(current_sum, 0) + 1
            
        return ans
