class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [None] * n
        char_idx = 0
        
        # 1. Faster Greedy Assignment
        for i in range(n):
            if res[i] is None:
                if char_idx >= 26: return ""
                curr_char = chr(97 + char_idx) # 97 is 'a'
                char_idx += 1
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        res[j] = curr_char
        
        if None in res: return ""
        s = "".join(res)
        
        # 2. Optimized O(1) Extra Space Verification
        # We check the LCP properties directly without a full DP table
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Basic LCP property: if chars match, LCP is 1 + next diagonal
                val = 0
                if s[i] == s[j]:
                    val = (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0) + 1
                
                # Check if calculated value matches the provided matrix
                if lcp[i][j] != val:
                    return ""
                    
        return s