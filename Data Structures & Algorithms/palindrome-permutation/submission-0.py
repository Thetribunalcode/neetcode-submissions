class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_set = set()

        for letter in s:
            if letter in char_set:
                char_set.remove(letter)
            else:
                char_set.add(letter)
        
        return len(char_set) <= 1