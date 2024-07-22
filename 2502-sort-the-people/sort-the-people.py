class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = [(names[i], heights[i]) for i in range(len(names))]
        temp.sort(key = lambda x:x[1], reverse = True)
        return [i for i, j in temp]
        