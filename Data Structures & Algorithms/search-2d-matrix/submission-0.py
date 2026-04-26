class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lst = []

        for i in matrix:
            lst += i
        print(lst)
        
        left = 0
        right = len(lst) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if lst[middle] == target:
                return True
            elif lst[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
                        
        return False