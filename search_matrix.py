from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        while l <= r:
            m = int((r+l)/2)
            row = m
            print(row)
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][0] < target: 
                l = m+1
            else:
                return True
        l, r = 0, len(matrix[row])-1
        while l <= r:
            m = int((r+l)/2)
            if matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] < target:
                l = m+1
            else:
                return True
            
        return False

Test = Solution()
print(Test.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]],
target=11))


        
