class Solution:
    def leftShift(self, s: str, n: int):
        string_list = list(s)
        for i in range(n):
            first_char = string_list[0]
            left_list = string_list[1:]
            left_list.append(first_char)
            string_list = left_list
        return "".join(string_list)

    def rightShift(self, s: str, n: int):
        string_list = list(s)
        for i in range(n):       
            last_char = string_list[-1]
            right_list = string_list[:-1]
            new_list = last_char + "".join(right_list)
            string_list = list(new_list)
        return "".join(string_list)
        
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        mutated_s = s
        for sublist in shift:
            if sublist[0] == 0:
                mutated_s = self.leftShift(mutated_s, sublist[1])
            elif sublist[0] == 1:
                mutated_s = self.rightShift(mutated_s, sublist[1])
        
        return mutated_s
                
        
        