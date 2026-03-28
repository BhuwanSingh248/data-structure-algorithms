class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [None] * n
        char_idx = 0
        
        # 1. Greedy Assignment
        for i in range(n):
            if res[i] is None:
                if char_idx >= 26: return ""  # Ran out of letters
                curr_char = chr(ord('a') + char_idx)
                char_idx += 1
                # Fill all positions that must be the same character
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = curr_char
        
        if None in res: return ""
        s = "".join(res)
        
        # 2. Verification via Dynamic Programming
        # We build the actual LCP of our string s to see if it matches input
        actual_lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    actual_lcp[i][j] = actual_lcp[i+1][j+1] + 1
                else:
                    actual_lcp[i][j] = 0
                
                # Check against original matrix immediately
                if actual_lcp[i][j] != lcp[i][j]:
                    return ""
                    
        return s