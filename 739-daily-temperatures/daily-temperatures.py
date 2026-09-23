class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        arr = [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < j:
                gi = stack.pop()
                arr[gi] =  i - gi
            stack.append(i)
        return arr