# find the target number with the minimum number of element from array  

def bestSum(targetSum, array, memo={}):
    if targetSum in memo.keys(): return memo[targetSum]
    if targetSum == 0 :return []
    if targetSum < 0 :return None 
    sortestComb = None
    for i in array:
        reminder  = targetSum - i
        remCombination =  bestSum(reminder, array)
        if remCombination != None:
            combination = remCombination + [i]
            if sortestComb == None or len(combination) < len(sortestComb):
                sortestComb = combination

    memo.update({targetSum:None})
    return sortestComb

print(bestSum(8,[2,3,5]))
