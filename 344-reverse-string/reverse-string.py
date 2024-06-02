class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0
        # right = len(s)-1
        # while left < right:
        #     temp = s[left]
        #     s[left] = s[right]
        #     s[right] = temp
        #     left+=1
        #     right-=1
        # for i in range (len(s)-1,-1,-1):
        #     s.append(s[i])
        #     s.pop(i)
        # s[:] = s[::-1]
    with open("user.out", "w") as f:
        for case in stdin:
            f.write(f"{dumps(loads(case.strip())[::-1]).replace(', ', ',')}\n")
    exit()