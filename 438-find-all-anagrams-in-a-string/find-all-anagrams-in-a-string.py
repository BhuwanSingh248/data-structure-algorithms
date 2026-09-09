class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        str_map_s = [0] * 26
        str_map_p = [0] * 26
        ans = []
        n, m = len(s), len(p)
        if m > n: return []
        
        for i in range(m):
            str_map_p[ord(p[i]) - ord('a')] += 1            
            str_map_s[ord(s[i]) - ord('a')] += 1

        for i in range(m, n):
            if str_map_s == str_map_p:
                ans.append(i-m)

            str_map_s[ord(s[i-m]) - ord('a')] -= 1
            str_map_s[ord(s[i]) - ord('a')] += 1 

        if str_map_s == str_map_p:
            ans.append(n - m)
        return ans