class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Helper function to check if a string is a palindrome
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        # Helper function for backtracking
        def backtrack(start: int, path: List[str]):
            # If we have reached the end of the string, add the current path to the result
            if start == len(s):
                result.append(path[:])
                return
            
            # Explore all possible partitions
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result
