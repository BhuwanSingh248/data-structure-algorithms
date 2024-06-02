class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, -1

        while( i <= len(s)//2 and abs(j) <= len(s)//2):
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        