class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in s:
            arr1[97 - ord(i)] += 1
        
        for i in t:
            arr2[97 - ord(i)] += 1

        return arr1 == arr2
