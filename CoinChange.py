from sys import maxsize
def printArr(d):
    for i in d:
        print(i)
def solution(coins, amt):
    n = len(coins)
    dp = [[0]*(amt+1) for j in range(n+1)]
    for i in range(n+1):
        for j in range(amt+1):
            if j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] =  1e5
            elif coins[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
    printArr(dp)
    return -1 if dp[n][amt] == maxsize else dp[n][amt]

a = solution([2,5,3,6], 10)
