class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        op = []
        candidates.sort()
        def helper(index, c_target, temp):
            if c_target == 0:
                op.append(list(temp))
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                if candidates[i] > c_target:
                    break

                temp.append(candidates[i])
                helper(i + 1, c_target - candidates[i], temp)
                temp.pop() # Backtrack

        helper(0, target, [])
        return op


