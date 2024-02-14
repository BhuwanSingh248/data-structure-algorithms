
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]
        # nums.sort()
        # return nums[ceil(len(nums) / 2) - 1]
    
        # optimizing the complixity
        
        candidate = None
        count = 0
        
        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if i == candidate else -1
        return candidate