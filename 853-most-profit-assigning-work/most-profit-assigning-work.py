class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxDifficulty = max(difficulty)
        maxProfitUpToDifficulty = [0] * (maxDifficulty + 1)

        for i in range(len(difficulty)):
            maxProfitUpToDifficulty[difficulty[i]] = max(maxProfitUpToDifficulty[difficulty[i]], profit[i])

        
        for i in range(1, maxDifficulty+1):
            maxProfitUpToDifficulty[i] = max(maxProfitUpToDifficulty[i], maxProfitUpToDifficulty[i-1])
        
        totalProfit = 0
        for i in worker:
            if i > maxDifficulty:
                totalProfit += maxProfitUpToDifficulty[maxDifficulty]
            else:
                totalProfit += maxProfitUpToDifficulty[i]
        return totalProfit