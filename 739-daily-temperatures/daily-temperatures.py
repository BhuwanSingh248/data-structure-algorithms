class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        arr = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and stack[-1][1] < j:
                gi, gj = stack.pop()
                arr[gi] =  i - gi
            stack.append((i, j))
        return arr