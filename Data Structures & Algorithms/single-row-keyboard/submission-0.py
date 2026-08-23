class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        time = 0
        letter_map = {}
        for i in range(len(keyboard)):
            letter = keyboard[i]
            letter_map[letter] = i
        
        prev_index = letter_map[word[0]]
        time += prev_index
        for letter in word[1:]:
            current_index = letter_map[letter]
            time += abs(current_index - prev_index)
            prev_index = current_index
        
        return time


            
            