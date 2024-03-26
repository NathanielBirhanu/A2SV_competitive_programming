class Solution:
    def freqAlphabets(self, s: str) -> str:
        e=""
        i = len(s)-1
        while i >=0 :
            if s[i] == "#":
                l = s[i-2:i]
                e = chr(int(l) + 96)+e
                i -= 3
            else:
                e = chr(int(s[i]) + 96)+e
                i -= 1
        return e
