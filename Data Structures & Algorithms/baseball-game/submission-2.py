class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_stack = []
        for operation in operations:
            match operation:
                case '+':
                    first_num = new_stack.pop()
                    second_num = new_stack.pop()
                    result = first_num + second_num
                    print(f'First Num: {first_num}, Second Num: {second_num}, Result: {result}')
                    new_stack.extend([second_num, first_num, result])
                case 'C':
                    popped_element = new_stack.pop()
                    print(f'Popped element: {popped_element}')
                case 'D':
                    item = new_stack.pop()
                    result = item * 2
                    print(f'Item: {item}, Result: {result}')
                    new_stack.extend([item, result])
                case _:
                    print('Default case', operation)
                    new_stack.append(int(operation))
        
        sum = 0

        for element in new_stack:
            sum += element
        
        return sum
        