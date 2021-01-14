# write a function that returns the combinition of numer that sum the targetSum 
# howSum(targetSum, array)


poss = []
def howSum(targetSum, array, memo = {}):
    if targetSum in memo.keys() : return memo[targetSum]
    if targetSum == 0 : return []
    if targetSum < 0 : return None
    for num in array:
        r = targetSum - num
        rem = howSum(r, array, memo)
        poss.append(rem)
        if (rem != None): 
            rem.append(num)
            memo.update({r : rem})
            return rem
    memo.update({targetSum : None})        
    return None

if __name__ == "__main__":
    print(howSum(7, [5, 3, 4, 7 ]))

    # print(poss)