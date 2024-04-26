class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001

        for numPassengers, start, end in trips:
            stops[start] += numPassengers
            stops[end] -= numPassengers

        passengers = 0
        for stop in stops:
            passengers += stop
            if passengers > capacity:
                return False

        return True
