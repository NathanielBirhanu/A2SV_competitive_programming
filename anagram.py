class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp = Counter(p)
        counts = Counter(s[:len(p)])
        my_list =[]
        l = 0
        r = len(p)
        while r < len(s):
            if countp == counts:
                my_list.append(l)
            counts[s[l]] -= 1
            if counts[s[l]] == 0:
                counts.pop(s[l])
            counts[s[r]] += 1
            l += 1
            r += 1
        if countp == counts:
            my_list.append(l)
        return my_list
            
        
        
