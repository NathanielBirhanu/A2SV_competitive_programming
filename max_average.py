class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        my_sum = sum(nums[:k])
        max_val = my_sum/k
        l = 0
        r = k
        while r < len(nums):
            my_sum -= nums[l]
            my_sum += nums[r]
            l += 1
            r += 1
            max_val = max(max_val, my_sum/k)
        return max_val
        
        

        
