from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_list = [row[0] for row in matrix]
        l, r = 0, len(row_list) - 1
        while l <= r:
            mid = (r + l) // 2
            if row_list[mid] == target:
                return True
            if row_list[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        row = l - 1
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
