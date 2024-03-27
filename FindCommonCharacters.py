class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        common_chars = []
        for char in set(words[0]):
            count = min(word.count(char) for word in words)
            common_chars.extend(char * count)
        return common_chars
