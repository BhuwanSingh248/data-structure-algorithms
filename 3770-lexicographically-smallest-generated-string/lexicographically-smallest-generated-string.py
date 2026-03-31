class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1
        res = [None] * total_len
        fixed = [False] * total_len
        
        # Step 1: Apply all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    idx = i + j
                    if res[idx] is not None and res[idx] != str2[j]:
                        return ""  # Contradiction found
                    res[idx] = str2[j]
                    fixed[idx] = True
        
        # Step 2: Fill non-fixed positions with 'a'
        for i in range(total_len):
            if res[i] is None:
                res[i] = 'a'
                
        # Step 3: Check 'F' constraints and fix violations
        for i in range(n):
            if str1[i] == 'F':
                # Check if the substring currently matches str2
                match = True
                for j in range(m):
                    if res[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # We must change one non-fixed character in this window
                    # Change the rightmost one to keep the string lexicographically small
                    changed = False
                    for j in range(m - 1, -1, -1):
                        idx = i + j
                        if not fixed[idx]:
                            # Try 'a', if it's already 'a' in str2, use 'b'
                            # Actually, it's already 'a' (from step 2), so if str2[j] == 'a', change to 'b'
                            res[idx] = 'b' if str2[j] == 'a' else 'a'
                            changed = True
                            break
                    
                    if not changed:
                        return "" # All chars in this 'F' window were fixed by 'T's
                        
        return "".join(res)