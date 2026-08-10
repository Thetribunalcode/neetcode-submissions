from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_dict = defaultdict(int)
        for char in s:
            new_dict[char]+=1
        for char in t:
            new_dict[char]-=1
        for keys, value in new_dict.items():
            if value: 
                return False
        return True