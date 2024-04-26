class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefixSum = 0
        remainderCounts = {0: 1}

        for num in nums:
            prefixSum = (prefixSum + num) % k
            if prefixSum in remainderCounts:
                count += remainderCounts[prefixSum]
            remainderCounts[prefixSum] = remainderCounts.get(prefixSum, 0) + 1

        return count
