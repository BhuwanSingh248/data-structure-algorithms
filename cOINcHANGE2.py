# find the number of possible ways to make a sum with inf. coins
def printlist(d):
    for i in d:
        print(i)

def solution(coins, amt):
    n = len(coins)
    dp = [[0]*(amt+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    # printlist(dp)
    for i in range(n+1):
        for j in range(amt+1):
            if j >= coins[i-1]:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    printlist(dp)
    return dp[n][amt]

solution([1,2,3,4,5], 3)