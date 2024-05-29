class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        # count = 0
        def helper(n, count):
            if n == 1:
                return count
            if n%2:
                return helper(n+1, count +1)
            
            else:
                return helper(n // 2, count + 1)
        
        return helper(n, 0)


