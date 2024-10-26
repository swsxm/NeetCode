from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_lookup = defaultdict(set)
        row_lookup = defaultdict(set)
        column_lookup = defaultdict(set)
        for y in range(9):
            for x in range(9):
                if board[y][x] == ".":
                    continue
                if board[y][x] in row_lookup[y]:
                    return False
                row_lookup[y].add(board[y][x])
                if board[y][x] in column_lookup[x]:
                    return False
                column_lookup[x].add(board[y][x])

                box_y = y // 3
                box_x = x // 3
                if board[y][x] in box_lookup[(box_y, box_x)]:
                    return False
                box_lookup[(box_y, box_x)].add(board[y][x])
        return True

# Testing the corrected code
Test = Solution()
board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(Test.isValidSudoku(board))
