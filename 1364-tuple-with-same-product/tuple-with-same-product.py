class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i != j:
                    mul = nums[i]*nums[j]
                    if mul in count:
                        count[mul] += 1
                    else :
                        count[mul] = 1
        result = 0
    # For each product, add the number of valid tuples.
        for k in count.values():
            if k > 1:
                result += 8 * (k * (k - 1) // 2)
        return result