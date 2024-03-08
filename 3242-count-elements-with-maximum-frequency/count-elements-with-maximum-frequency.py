class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        nums_common = nums_count.most_common()
        ans = nums_common[0][1]
        for i in range(1,len(nums_common)):
            if nums_common[i][1] == nums_common[0][1]:
                ans += nums_common[i][1]
            else:
                break
        return ans 
            
