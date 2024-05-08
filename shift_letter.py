class Solution:
    def shiftingLetters(self, s, shifts: list[list[int]]) -> str:
        arr = [0] * (len(s) + 1)
        for start, end, direction in shifts:
            num = 1 if direction == 1 else -1
            arr[start] += num
            arr[end + 1] -= num

        res = ''
        for i in range(len(s)):
            if i != 0:
                arr[i] = arr[i] + arr[i - 1]
            c = (ord(s[i]) - ord('a') + arr[i]) % 26 + ord('a')
            res += chr(c)
        return res
