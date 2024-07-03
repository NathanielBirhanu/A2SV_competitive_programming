class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        def canShip(mid):
            ship, currMid = 1, mid
            for weight in weights:
                if currMid - weight < 0:
                    ship += 1
                    currMid = mid
                currMid -= weight
            return ship <= days

        while l <= r:
            mid = (l+r)//2
            if canShip(mid):
                res = min(res, mid)
                r = mid -1
            else:
                l = mid + 1
        return res
        
