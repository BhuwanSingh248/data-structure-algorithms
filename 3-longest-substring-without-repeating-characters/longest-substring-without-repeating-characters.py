class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = 0
        nx = 0
        n = len(s)
        max_len = 0
        rec = set()
        while nx < n:
            if s[nx] in rec:
                max_len = max(max_len, nx - st)
                rec.remove(s[st])
                st += 1
            else:
                rec.add(s[nx])
                nx+=1
        max_len = max(max_len, nx - st)
        return max_len
