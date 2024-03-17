class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = bisect_left(intervals, newInterval)
        intervals.insert(index, newInterval)
        stack = []
        for i, j in intervals:
            # will push data to stack if no calculation needed 
            # if top of the stack have end value > then start of next value
            if stack and stack[-1][1] >= i:
                a,b = stack.pop()
                stack.append([a, max(b, j)])
            else:
                stack.append([i,j])
        return stack