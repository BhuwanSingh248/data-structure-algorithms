int maxSubArray(int* nums, int numsSize) {
    int maxsum = -10000;
    int sum = 0;
    for(int i = 0; i<numsSize; i++)
    {
        if(sum >=0)
        sum+=nums[i];
        else 
        sum = nums[i];
        if(sum>maxsum)
        maxsum=sum;
    }
    return maxsum;
}