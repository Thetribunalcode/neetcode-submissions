class Solution:
    def countElements(self, arr: List[int]) -> int:
        element_map = {}

        for element in arr:
            if element in element_map:
                element_map[element] += 1
            else: 
                element_map[element] = 0

        cnt = 0
        for element in arr: 
            if (element+1) in element_map:
                cnt += 1
        
        return cnt
        