class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l1 = 0
        l2 = 0
        count = 0
        while l1 < len(players) and l2 < len(trainers):
            if players[l1] <= trainers[l2]:
                count += 1
                l1 += 1
                l2 += 1
            else:
                l2 += 1
        return count

        
