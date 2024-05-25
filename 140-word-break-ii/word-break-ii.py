class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        unique_word = set(wordDict)
        result = []
        
        def helper(s, current, start):
            nonlocal unique_word
            nonlocal result
            if start == len(s):
                result.append(" ".join(current))
                return None
                
            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in unique_word:
                    current.append(word)
                    
                    helper(s, current, end)
                    current.pop()
        helper(s, [],  0)
        return result