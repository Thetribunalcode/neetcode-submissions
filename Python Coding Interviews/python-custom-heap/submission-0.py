import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    new_list = []
    for num in nums:
        pair = ( -num, num )
        heapq.heappush(max_heap, pair)
    while max_heap:
        pair = heapq.heappop(max_heap)
        new_list.append(pair[1])
    return new_list

    
    pass



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
