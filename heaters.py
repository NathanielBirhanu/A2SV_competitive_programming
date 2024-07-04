class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def dist_closest(heaters, house):
            l, r = 0, len(heaters)-1
            min_dist = float('inf')
            while l<= r:
                mid = (l+r)//2
                min_dist = min(min_dist, abs(heaters[mid] - house))
                if heaters[mid] < house:
                    l = mid + 1
                else:
                    r = mid -1
            return min_dist
        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius, dist_closest(heaters, house))
        return radius        


        
