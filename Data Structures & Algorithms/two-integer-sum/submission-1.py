class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            element_to_find = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == element_to_find:
                    new_list.append(i)
                    new_list.append(j)
                    break
        return new_list
