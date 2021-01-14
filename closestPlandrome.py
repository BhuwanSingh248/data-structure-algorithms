def isPlaindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

a = "90"
temp = len(a)//2
temp_a = a[:temp][::-1]
out = ""
out2 = ""
if len(a)%2 == 0:
    if isPlaindrome(int(a)+2):
        out=str(int(a)+2)
    else:
        out = a[:temp]+temp_a
        if a == out:
            out = a[:temp-1] + str(int(a[temp-1])-1)+str(int(a[temp])-1) + temp_a[1:]
            if out == "00":
                out = str(int(a)-2)
else:
    out = a[:temp]+a[temp]+temp_a
    if a == out:
        out = a[:temp]+str(int(a[temp])-1)+temp_a

out2 = 2*int(a) - int(out)
print(out)


    # def nearestPalindromic(self, a: str) -> str: 
    #     if a == "1":
    #         return "0"
    #     def isPlaindrome(n):
    #         n = str(n)
    #         if n == n[::-1]:
    #             return True
    #         return False
    #     if len(a) == 2 and 
    #     temp = len(a)//2
    #     temp_a = a[:temp][::-1]
    #     out = ""
    #     out2 = ""
    #     if len(a)%2 == 0:
    #         out = a[:temp]+temp_a
    #         if a == out:
    #             out = a[:temp-1] + str(int(a[temp-1])-1)+str(int(a[temp])-1) + temp_a[1:]
    #             if out == "00":
    #                 out = str(int(a)-2)
    #     else:
    #         out = a[:temp]+a[temp]+temp_a
    #         if a == out:
    #             out = a[:temp]+str(int(a[temp])-1)+temp_a

    #     out2 = 2*int(a) - int(out)
    #     if isPlaindrome(out2):
    #         return str(min(int(out2), int(out)))
    #     return out