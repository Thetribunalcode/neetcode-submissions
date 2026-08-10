class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        new_list = []
        for key, num in enumerate(nums):
            element_to_find = target - num
            if element_to_find in hashMap:
                new_list.append(hashMap[element_to_find])
                new_list.append(key)
            else:
                hashMap[num] = key
        return new_list