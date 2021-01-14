nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def sortArr(nums1, nums2):
    for i in range(len(nums2)):
        nums1[len(nums2)+i] = nums2[i]
    nums1 =sorted(nums1)
    return(nums1)
print(sortArr(nums1, nums2))