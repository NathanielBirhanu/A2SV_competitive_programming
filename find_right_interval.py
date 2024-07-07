class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarySearch(interval_with_index, end_time):
            l, r= 0, len(interval_with_index)-1
            res = -1
            while l <= r:
                mid = (l+r)//2
                if interval_with_index[mid][0] >= end_time:
                    res = interval_with_index[mid][2]
                    r = mid -1
                else:
                    l = mid + 1
            return res


        interval_with_index = [(interval[0], interval[1], index)for index, interval in enumerate(intervals)]
        interval_with_index.sort()

        result = []
        for interval in intervals:
            end_time = interval[1]
            index = binarySearch(interval_with_index, end_time)
            result.append(index)
        return result
