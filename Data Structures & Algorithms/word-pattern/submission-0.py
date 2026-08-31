class Solution:
    def getWordMatch(self, pattern: str, s: str) -> bool:
        wordMap = {}
        str_list = s.split(' ')
        if len(pattern) != len(str_list):
            return False  
        for word, char in zip(str_list, pattern):
            if word in wordMap:
                if wordMap[word] != char:
                    return False
            else:
                wordMap[word] = char
        return True
    
    def getPatternMatch(self, pattern: str, s: str) -> bool:
        wordMap = {}
        str_list = s.split(' ')
        if len(pattern) != len(str_list):
            return False  
        for word, char in zip(str_list, pattern):
            if char in wordMap:
                if wordMap[char] != word:
                    return False
            else:
                wordMap[char] = word
        return True
    def wordPattern(self, pattern: str, s: str) -> bool:
        return self.getWordMatch(pattern, s) and self.getPatternMatch(pattern, s)

        