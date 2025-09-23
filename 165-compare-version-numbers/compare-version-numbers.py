class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))            
        itr = range(max(len(ver1), len(ver2)))
        for i in itr:
            v1, v2 = 0, 0
            if i < len(ver1):
                v1 = ver1[i]
            if i < len(ver2):
                v2 = ver2[i]

            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        else:
            return 0