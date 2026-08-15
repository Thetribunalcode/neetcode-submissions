class Solution:
    def confusingNumber(self, n: int) -> bool:
        new_n = str(n)
        not_allowed_chars = ['2','3','4','5','7']
        allowed_chars = []
        for char in new_n:
            if char in not_allowed_chars:
                return False
            if char == '0':
                allowed_chars.append('0')
            elif char == '1':
                allowed_chars.append('1')
            elif char == '6':
                allowed_chars.append('9')
            elif char == '8':
                allowed_chars.append('8')
            elif char == '9':
                allowed_chars.append('6')
        new_number = int("".join(sorted(allowed_chars)))
        if new_number == n:
            return False
        else:
            return True