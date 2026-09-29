class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
            n = len(heights)
            pse = [-1] * n
            nse = [n] * n
            stack = []

            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    inx = stack.pop()
                    nse[inx] = i 

                if stack:
                    pse[i] = stack[-1]

                stack.append(i) 
            max_area = 0
            for i in range(n):
                max_area = max(max_area, heights[i] * (nse[i] - pse[i] - 1))
            return max_area