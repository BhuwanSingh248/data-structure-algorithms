class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = []
        def is_sorted(array:List[int]) -> bool:
            for i in range(1, len(array)):
                if array[i-1] > array[i]:
                    return False
            else:
                return True
        start  = 1
        if is_sorted(nums):
            return True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                start = i
                break
        arr = nums[start+1:len(nums)] + nums[0: start+1]
        print(arr)
        return is_sorted(arr)
                
            