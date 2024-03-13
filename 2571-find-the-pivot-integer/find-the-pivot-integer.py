class Solution:
    def pivotInteger(self, n: int) -> int:
        sol = sqrt(n*(n+1)/2)
        if sol%1 !=0:
            return -1
        return int(sol)