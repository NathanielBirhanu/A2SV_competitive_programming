class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeroCount = 0
        maxConsecutive = 0
        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
            if zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxConsecutive = max(maxConsecutive, right - left + 1)
            right += 1
        return maxConsecutive


