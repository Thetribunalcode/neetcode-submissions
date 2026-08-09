class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_element = -1
            for j in range(i+1, len(arr)):
                max_element = max(arr[j], max_element)
            arr[i] = max_element
        return arr
        