class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        my_list=[]
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                my_list.append(i)
        return my_list
