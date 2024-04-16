class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l = 0
        m = 0
        merge = []
        while l < len(word1) and m < len(word2):
            if ord(word1[l]) > ord(word2[m]):
                merge.append(word1[l])
                l += 1
            elif ord(word1[l]) < ord(word2[m]):
                merge.append(word2[m])
                m += 1
            else:
                if word1[l:] > word2[m:]:
                    merge.append(word1[l])
                    l += 1
                else:
                    merge.append(word2[m])
                    m += 1
        merge.extend(word1[l:])
        merge.extend(word2[m:])
        return ''.join(merge)
