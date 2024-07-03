class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if  l < len(nums) and nums[l] == target:
            return l
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        
