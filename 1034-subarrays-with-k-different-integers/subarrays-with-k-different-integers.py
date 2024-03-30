class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(k):
            u = {}
            i, j = 0, 0
            count = 0
            ans = 0
            while j < len(nums):
                if nums[j] in u:
                    u[nums[j]] += 1
                else:
                    u[nums[j]] = 1
                while len(u) > k:
                    u[nums[i]] -= 1
                    if u[nums[i]] == 0:
                        del u[nums[i]]            
                    i += 1
                ans += j-i+1
                j += 1
            return ans

        return helper(k) - helper(k-1)