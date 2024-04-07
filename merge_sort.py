class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        
        p1 = 0
        p2 = 0
        p = 0
        
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1
        while p1 < m:
            nums1[p] = nums1_copy[p1]
            p1 += 1
            p += 1
        while p2 < n:
            nums1[p] = nums2[p2]
            p2 += 1
            p += 1
