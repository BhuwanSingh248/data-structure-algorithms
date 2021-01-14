a = [1, 2, 1, 2]
k = 3
count, total = 0, 0 
mapDict = {}
mapDict.update({0:1})
for i in range(len(a)):
    total += a[i]
    if total-k in mapDict.keys():
        count += mapDict[total-k]
    mapDict.update({total: mapDict.get(total, 0)+1})
    print(mapDict)
print(count)
