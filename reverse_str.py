class Solution:
    def reverseVowels(self, s: str) -> str:
    
        vowels = "aeiouAEIOU"
        s_list = list(s)
        l = 0
        r = len(s_list) - 1
        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowels:
                r -= 1
            else:
                l +=1
        return ''.join(s_list)


        
