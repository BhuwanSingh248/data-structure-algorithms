class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = [[]]
        last_size = 0
        for i in range(len(nums)):
            start = last_size if i > 0 and nums[i] == nums[i-1] else 0
            current_size = len(op)

            for j in range(start, current_size):
                op.append(op[j] + [nums[i]])
            
            last_size = current_size
        return op