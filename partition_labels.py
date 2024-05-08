class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp ={}
        for i, c in enumerate(s):
            mp[c] = i
        size, end = 0, 0
        ans = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, mp[c])
            if i == end:
                ans.append(size)
                size = 0
        return ans

        
        
