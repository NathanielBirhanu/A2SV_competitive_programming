class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        l = 0
        m = 0
        while l < len(nums1) and m < len(nums2):
            if nums1[l] == nums2[m]:
                return nums1[l]
            elif nums1[l] > nums2[m]:
                m += 1
            else:
                l += 1
        return -1
                
        
