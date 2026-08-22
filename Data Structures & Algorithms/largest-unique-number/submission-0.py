from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        numMap = defaultdict(int)
        largest_num = -1
        for num in nums:
            numMap[num] += 1
        
        sorted_numMap = dict(sorted(numMap.items(), reverse=True))
        print(sorted_numMap)
        
        for key, value in sorted_numMap.items():
            if value > 1:
                continue
            return key
        
        return -1