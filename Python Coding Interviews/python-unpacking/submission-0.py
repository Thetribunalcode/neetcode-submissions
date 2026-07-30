from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    num1, num2, num3 = triplet
    return num1 + num2 + num3
    pass


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    dim1, dim2, dim3 = box_dimensions
    return dim1 * dim2 * dim3
    pass
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
