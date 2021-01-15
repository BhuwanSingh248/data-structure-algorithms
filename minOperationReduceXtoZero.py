def minOperations(nums:list, x:int)-> int :
    n = len(nums)
    sum = 0
    mymap = {}
    for i in range(n):
        sum+=nums[i]
        mymap.update({sum:i})
    if x > sum:
        return -1 
    mymap.update({0:0})
    print(mymap)
    longest = 0
    sum -= x
    val = 0
    for i in range(n):
        val += nums[i]
        if val-sum in mymap.keys():
            longest = max(longest, i-mymap[val-sum]+1) if val-sum == 0 else max(longest, i-mymap[val-sum])
    return (n if sum==0 else -1) if longest == 0 else n-longest

print(minOperations([8,1,4,2,7], 6))