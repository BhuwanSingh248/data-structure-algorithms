class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i != ")":
                stack.append(i)
            
            else:
                temp = ""
                val = stack[-1]
                while stack:
                    val = stack.pop()
                    if val == "(":
                        break
                    temp += val
                stack.append(temp[::-1])
        ans = ""
        while stack:
            val = stack.pop()
            if val != "(":
                ans += val
        return ans[::-1]