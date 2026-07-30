from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for index, item in enumerate(nums):
        if item == 7:
            return index
    return -1
    pass


def get_dist_between_sevens(nums: List[int]) -> int:
    occurence_count = 0
    first_index = 0
    second_index = 0
    for index, number in enumerate(nums):
        if number == 7:
            if occurence_count == 0:
                occurence_count += 1
                first_index = index
            else:
                occurence_count += 1
                second_index = index
                break
        else:
            pass
    return second_index - first_index
    pass


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
