class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both arrays to apply greedy approach
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        # Iterate while there are children left to satisfy and cookies left to give
        while child_i < len(g) and cookie_j < len(s):
            # If the cookie can satisfy the child
            if s[cookie_j] >= g[child_i]:
                child_i += 1  # Move to the next child
            
            # Move to the next cookie regardless
            cookie_j += 1
            
        return child_i