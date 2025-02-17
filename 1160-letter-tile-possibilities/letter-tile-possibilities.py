class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = {}
        for i in tiles:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        ans = 0
        def helper(ctr):
            ans = 0
            for i in ctr:
                if ctr[i] > 0:
                    ctr[i] -= 1
                    ans += 1+ helper(ctr)
                    ctr[i] += 1
            return ans
        return helper(counter)