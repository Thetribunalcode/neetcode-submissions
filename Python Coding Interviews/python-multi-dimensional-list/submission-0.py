from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_item = -1
    new_list = []
    for sublist in nested_arr: 
        for item in sublist:
            max_item = max(item, max_item)
        new_list.append(max_item)
        max_item = -1
    return new_list
    pass


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
