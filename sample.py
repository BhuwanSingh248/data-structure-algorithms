a = [1, 2, 4, 67,67, 54, 34, 89, 89]
first,second = -1, -1
temp = a[0]
for i in a:
    if temp < i:
        temp = i
    if first < temp:
        first  = temp
    elif first > second:
        second = temp
print(first, second)
