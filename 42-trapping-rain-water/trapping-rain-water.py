class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        fe = [0] * n
        ef = [0] * n
        prev = height[0]
        fe[0] = prev
        ef[-1] = prev
        for i in range(1, n):
            prev = max(prev, height[i])
            fe[i] = prev
        prev = height[-1]
        ef[-1] = prev
        for i in range(n-2, -1, -1):
            prev = max(prev, height[i])
            ef[i] = prev
        
        total = 0
        for i, (j, k) in enumerate(zip(fe, ef)):
            total += min(j, k) - height[i]
        return total