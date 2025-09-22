class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                 counter[i] = 1

        max_element = max(counter.values())
        count = list(counter.values()).count(max_element)
        return count * max_element