class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        m = len(people)-1
        count = 0
        while l <= m:
            my_sum = people[l]+people[m]
            if my_sum > limit:
                if people[m] >= people[l]:
                    count += 1
                    m -= 1
                
                else:
                    count +=1
                    l += 1
            else:
                count += 1
                l += 1
                m -= 1
        return count

