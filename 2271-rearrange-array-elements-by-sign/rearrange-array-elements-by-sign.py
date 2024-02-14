class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        parr = []
        narr = []
        arr = []
        for i in nums:
            if i > 0:
                parr.append(i)
            if i < 0:
                narr.append(i)
        
        for i in range(len(parr)):
            arr.append(parr[i])
            arr.append(narr[i])
        return arr
            