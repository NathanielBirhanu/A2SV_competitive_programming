class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {"(":")", "{":"}", "[":"]"}
        for i in range(len(s)):
            if s[i] in mp.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                n = stack.pop()
                if s[i] != mp[n]:
                    return False
        return stack == []
        
