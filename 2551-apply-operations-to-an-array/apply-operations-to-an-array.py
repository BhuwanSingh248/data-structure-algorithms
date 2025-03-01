class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # if num[i] ==  num[i+1] --> num[i] *= 2 and num[i+1] = 0
        # shift 0 at end of array 


        st = 0
        ed = 1
        end = -1
        while ed < len(nums):
            if nums[st] == nums[ed]:
                nums[st] *= 2
                nums[ed] = 0
            st+=1
            ed += 1

        temp = list(filter(lambda i:i>0, nums)) 
        temp.extend([0] * (len(nums) - len(temp)))
        return temp