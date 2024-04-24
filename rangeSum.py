class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] *(len(nums)+1)
        self.prefix_sum[0] = nums[0]
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        sumLeft = self.prefix_sum[left]
        sumRight = self.prefix_sum[right+1]
        return sumRight - sumLeft
