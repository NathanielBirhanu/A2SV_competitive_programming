class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)-1
        while l < r:
            mid = (l+r)//2
            if ord(letters[mid]) > ord(target):
                r = mid
            elif ord(letters[mid]) <= ord(target):
                l = mid + 1
        if ord(letters[l]) > ord(target):
            return letters[l]
        else:
            return letters[0]
        
