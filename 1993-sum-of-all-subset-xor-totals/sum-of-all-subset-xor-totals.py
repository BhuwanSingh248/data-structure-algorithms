from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(0, n+1):
            ans += self.calculate_xor(combinations(nums, i))
                
        return ans 

    def calculate_xor(self, arr:List[int]):
        ans = 0
        # print(arr)
        for i in arr:
            xor = 0
            for j in i:
                xor ^= j
            print(list(i), ":"  ,xor)
            ans += xor
        return ans


