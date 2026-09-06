class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = set()
        st = 0
        end = 0
        n = len(s)
        ans = 1 if n else 0
        while end < n:
            if s[end] not in mem:
                mem.add(s[end])
                end += 1
            else:
                mem.remove(s[st])
                st += 1
            ans = max(ans, end - st)

        return ans