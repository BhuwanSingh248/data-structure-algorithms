s1 = "ab"
s2 = "eidbaooo"
s3 = []
length = len(s1)
def check(a, b):
    return sorted(list(a)) == sorted(list(b))

for i,j in enumerate(s2):
    if j in s1:

        check(s2[i:i+length], s1)