class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = {j:i for i, j in enumerate(sorted(score, reverse = True))}
        ans = []
        for i in score:
            if temp[i] == 0: ans.append('Gold Medal')
            elif temp[i] == 1: ans.append('Silver Medal')
            elif temp[i] == 2: ans.append('Bronze Medal')
            else: ans.append(str(temp[i]+1))
        return ans


        