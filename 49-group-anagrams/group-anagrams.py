class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            temp = "".join(sorted(list(i)))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        return list(dic.values())