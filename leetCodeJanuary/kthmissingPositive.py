arr = [2,3,4,7,11]
k = 5

def findkthpositive(arr, k):
    arr.insert(0,0)
    i = 0
    max_len = len(arr)
    while k >= 0 and i <= max_len-2:
        k -= arr[i+1]-arr[i]-1
        if k <= 0:
            return arr[i+1] + k - 1
        i+=1
    return arr[max_len-1]+k


print("op: ",findkthpositive(arr, k))