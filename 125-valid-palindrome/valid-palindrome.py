class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = ''
        for i in s:
            arr += i.lower() if i.isalnum() else ""
        print(arr)
        return arr == arr[::-1]

        