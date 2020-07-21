def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.remove(0)
    nums1.extend(nums2)
    nums1.sort()
    return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))