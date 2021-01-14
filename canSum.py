# canSum(targeTsum, array) --> @ return true is any numbers in array sums targetsum else False

def canSum(targetSum, array, mem = {}):
    if targetSum in mem : return mem[targetSum]
    if targetSum == 0 : return True
    if targetSum < 0 : return False
    for i in array:
        r = targetSum - i
        if canSum(r, array) == True: 
            mem.update({targetSum:True})
            return True
    mem.update({targetSum:False})
    return False



print(canSum(300,[7,14]))