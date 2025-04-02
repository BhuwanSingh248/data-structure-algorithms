class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        a,b,c = 0, 0, 0
        n = len(nums)
        ans = 0
        for i in range(n-2):
            a = nums[i]
            for j in range(i+1,n):
                b = nums[j]
                for k in range(j+1, n):
                    c = nums[k]
                    ans = max(ans, (a-b)*c)
        return ans