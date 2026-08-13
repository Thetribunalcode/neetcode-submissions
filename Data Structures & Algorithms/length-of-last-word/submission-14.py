class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed_list = s.strip()
        word_list = trimmed_list.split(" ")
        length = len(word_list[-1])
        return length