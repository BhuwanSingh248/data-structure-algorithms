class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        dic = {}
        cc = 1
        for i in arr2:
            if i not in dic:
                dic[i] = cc
                cc += 1
            
        
        for i,j in enumerate(arr):
            arr[i] = dic[j]
            
        return arr