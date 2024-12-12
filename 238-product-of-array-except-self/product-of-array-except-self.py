class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        is_negative = False
        is_zero = 0
        prod = 1
        
        for i in nums:
            if i < 0:
                is_negative = not is_negative
            if i == 0:
                is_zero += 1
            
            else:
                prod *= i
        print(prod)
        if is_zero > 1:
            return [0] * len(nums)
        ans = []        
        for i in nums:
            temp = 0
            if i != 0 and is_zero == 0:
                temp = prod // i
            if i == 0:
                temp = prod
            
            ans.append(temp)
        return ans