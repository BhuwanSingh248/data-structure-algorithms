class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        m, n = len(nums1), len(nums2)
        ans = []
        while ptr1 < m or ptr2 < n:
            i, j, k, l = None, None, None, None
            if ptr1 < m:
                i, j = nums1[ptr1]
            if ptr2 < n:
                k, l = nums2[ptr2]
            
            if i and k:
                if i < k:
                    ans.append([i, j])
                    ptr1 += 1
                elif i > k:
                    ans.append([k, l])
                    ptr2 += 1
                else:
                    ans.append([i, l+j])
                    ptr1 += 1
                    ptr2 += 1

            elif i:
                ans.append([i, j])
                ptr1 += 1
            else:
                ans.append([k, l])
                ptr2 += 1
        return ans 