class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def helper(idx, current_amount):
            # Check memo with the full state (idx AND amount)
            if (idx, current_amount) in memo:
                return memo[(idx, current_amount)]
            
            # Base Cases
            if current_amount == 0:
                return 0
            if current_amount < 0 or idx == len(coins):
                return float('inf')
            
            # 1. Include current coin (stay at idx to allow infinite use)
            res_include = 1 + helper(idx, current_amount - coins[idx])
            
            # 2. Exclude current coin (move to next index)
            res_exclude = helper(idx + 1, current_amount)
            
            memo[(idx, current_amount)] = min(res_include, res_exclude)
            return memo[(idx, current_amount)]

        ans = helper(0, amount)
        return ans if ans != float('inf') else -1