class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        count = 1
        end = points[0][1]

        for i, j in points[1:]:
            if end < i:
                count+=1
                end = j
            end = min(j, end)
        return count