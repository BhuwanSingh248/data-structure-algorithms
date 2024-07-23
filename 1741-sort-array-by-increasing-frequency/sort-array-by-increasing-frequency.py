class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        data = {}
        for i in nums:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        
        return sorted(nums, key = lambda x:(data[x], -x))