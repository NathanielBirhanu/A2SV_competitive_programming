class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        summ =0
        
        while l < r:
            my_sum = skill[l] + skill[r]
            if (skill[l+1] + skill[r-1]) == my_sum:
                summ += skill[l] * skill[r]
                l+=1
                r-=1
            else:
                return -1
        return summ
        

        
