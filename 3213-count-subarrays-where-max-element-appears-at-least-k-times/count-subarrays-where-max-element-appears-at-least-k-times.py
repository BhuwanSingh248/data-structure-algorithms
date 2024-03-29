class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        freq = 0
        i,j = 0, 0
        ans = 0
        n = len(nums)
        while j < n:
            if nums[j] == max_element:
                freq += 1
            while freq >= k:
                ans += n - j
                if nums[i] == max_element:
                    freq -= 1
                i+=1
            j+=1
        return ans 