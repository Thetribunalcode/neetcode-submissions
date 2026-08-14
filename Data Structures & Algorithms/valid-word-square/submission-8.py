class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        i, j = 0, 0
        while i < len(words):
            j = 0
            print(f'i = {i}')
            while j < len(words[i]):
                print(f'j = {j}')
                if (len(words) - 1) < j:
                    return False
                if (len(words[j]) - 1 ) < i:
                    return False
                if words[i][j] != words[j][i]:
                    return False
                j += 1
            i += 1
        return True

                