class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        a,b,c = 0, 0, 0
        for i in nums:
            a = max(a, b * i)
            b = max(b, c - i)
            c = max(c, i)
        return a