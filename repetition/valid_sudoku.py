from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_row = defaultdict(list)
        check_column = defaultdict(list)
        check_box = defaultdict(list)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == ".":
                    continue

                if board[y][x] in check_row[y]:
                    return False

                if board[y][x] in check_column[x]:
                    return False

                box_y = y // 3
                box_x = x // 3
                pos = tuple([box_y, box_x])

                if board[y][x] in check_box[pos]:
                    return False

                check_box[pos].append(board[y][x])
                check_row[y].append(board[y][x])
                check_column[x].append(board[y][x])
        return True
