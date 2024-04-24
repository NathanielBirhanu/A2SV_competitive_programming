from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        # Calculate products of elements to the left
        product = 1
        for i in range(n):
            answer[i] = product
            product *= nums[i]

        # Calculate products of elements to the right and combine with left products
        product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer
