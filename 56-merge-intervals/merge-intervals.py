class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = []
        st, ed = intervals[0]
        for i, j in intervals[1:]:
            
            if i <= ed :
                ed = max(ed, j)
                # continue
            else:
                merged.append([st, ed])
                st, ed = i, j

        merged.append([st, ed])
        return merged