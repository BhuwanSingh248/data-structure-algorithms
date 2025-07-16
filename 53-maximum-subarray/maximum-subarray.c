int maxSubArray(int* nums, int numsSize) {
    int sum = 0,prevsum= -1000000;
    for(int i=0; i<numsSize; i++){
        int tot = sum + nums[i];
        if(nums[i] > tot) sum = nums[i];
        else sum = tot;
        if(prevsum < sum) prevsum = sum ;

    }
    return prevsum; 
}