a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubarraySum(array: list):
    from sys import maxsize
    resultSum = -(maxsize-1)
    tempSum = 0
    for j, i in enumerate(array):
        tempSum = max(i, i + tempSum)
        if tempSum > resultSum:
            print(j)
            resultSum = tempSum
    return resultSum

b = maxSubarraySum(a)
print(b)



