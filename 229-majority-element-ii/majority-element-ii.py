class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        maj_1, maj_2 = None, None
        count_1, count_2 = 0, 0
        for i in nums:
            if count_1 != 0 and maj_1 == i:
                count_1 += 1
            elif count_2 != 0 and maj_2 == i:
                count_2 += 1
            elif count_1 == 0:
                maj_1 = i
                count_1 += 1
            elif count_2 == 0:
                maj_2 = i
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1
        count_1, count_2 = 0, 0
        n = len(nums)
        ans = []
        for i in nums:
            if i == maj_1:
                count_1 += 1
            elif i == maj_2:
                count_2 += 1
        if count_1 > n / 3:
            ans.append(maj_1)
        if count_2 > n / 3:
            ans.append(maj_2)
        return ans