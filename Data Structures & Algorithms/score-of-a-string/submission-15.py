class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        i = 0
        if len(s) == 0 or len(s) == 1:
            return sum
        while i < len(s) - 1:
            diff = ord(s[i]) - ord(s[i+1])
            sum += abs(diff)
            i += 1
        return sum

        