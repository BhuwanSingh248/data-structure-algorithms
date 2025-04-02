class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        mem = set()
        ans = 1 if s else 0
        while end < len(s):
            if s[end] not in mem:
                mem.add(s[end])
                end += 1
            else:
                mem.remove(s[start])
                start += 1
            ans = max(ans, end-start)
        return ans

