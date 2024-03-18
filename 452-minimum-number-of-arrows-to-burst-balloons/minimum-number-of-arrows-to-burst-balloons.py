class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        start, end = points[0]

        for i, j in points[1:]:
            if end < i:
                count+=1
                end = j
            
            start = min(i, start)
            end = min(j, end)
        return count