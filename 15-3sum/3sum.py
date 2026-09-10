class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            seen = set()
            j = i + 1
            while j < len(nums):
                target = -nums[i] - nums[j]
                if target in seen:
                    ans.append([nums[i], target, nums[j]])
                    # Skip duplicates for the second element
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1
                
        return ans