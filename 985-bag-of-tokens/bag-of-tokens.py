class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        scr = 0
        max_scr = 0
        l = 0
        r = n - 1
        
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                scr += 1
                l += 1
                max_scr = max(max_scr, scr)
            elif scr > 0:
                power += tokens[r]
                scr -= 1
                r -= 1
            else:
                break
                
        return max_scr