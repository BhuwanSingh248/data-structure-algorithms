class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        ans = 0
        isodd = 0
        for i, j in dic.items():
            if j %2 ==0:
                ans += j
            else:
                if j >= 1:
                    ans += j-1
                isodd = 1
        ans += isodd
        return ans 

