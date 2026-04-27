class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        # def helper(index, target, temp):
        #     if target == 0:
        #         res.append(temp)
        #         return

        #     if index >= len(candidates):
        #         return 
            

        #     helper(index + 1, target, temp[:])

        #     new_target = target - candidates[index]
        #     if new_target >= 0:
        #         temp.append(candidates[index])
        #         helper(index, new_target, temp)
                
        def helper(index, target, path):
            if target == 0: 
                res.append(path)
                return

            for i in range(index, len(candidates)):
                if candidates[index] > target:
                    break
                
                helper(i, target - candidates[i], path + [candidates[i]])
        helper(0, target, [])
        return res
