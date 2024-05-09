class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        ans = 0
        index = 0
        for i in range(k):
            temp = happiness[index] - index
            if temp >= 0:
                ans += temp
            index += 1
        return ans
