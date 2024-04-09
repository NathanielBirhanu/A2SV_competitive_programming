class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0 
        r = len(nums)-1
        count = 0
        while l < r:
            my_sum = nums[l] + nums[r]
            if my_sum == k:
                count += 1
                r -= 1
                l +=1
            elif my_sum > k:
                r -= 1
            else:
                l += 1
        return count

        
