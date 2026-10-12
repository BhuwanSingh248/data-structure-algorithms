class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ele = nums[0]
        count = 0
        for i in nums:
            if count == 0: 
                if i != ele:
                    ele = i
                count += 1
            else:
                if i!= ele:
                    count -= 1
                else:
                    count +=1    
        return ele


