class Solution:
    @lru_cache
    def maximumOddBinaryNumber(self, s: str) -> str:
        once = s.count('1') - 1
        return ('1' * once) + ('0' * (len(s) - once-1)) + ('1' if once >= 0 else '')
        

