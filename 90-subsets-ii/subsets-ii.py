class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # op = [[]]
        # last_index = 0

        # for i in range(len(nums)):
        #     start = last_index if i > 0 and nums[i] == nums[i-1] else 0
        #     current_size = len(op)
        #     for j in range(start, current_size):
        #         op.append(op[j] + [nums[i]])
            
        #     last_index = current_size
        
        # return op

        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(list(path))

            for i in range(start, len(nums)):
                if i> start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res