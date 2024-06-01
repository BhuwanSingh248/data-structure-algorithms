class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) < 2:
            return 
        
        i,j = 0, 1
        
        ans = 0
        while j < len(s):
            ans += abs(ord(s[i])-ord(s[j]))
            i+=1
            j+=1
        
        return ans 
