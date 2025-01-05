# Valid Sudoku
# You are given a a 9 x 9 Sudoku board board. A Sudoku board is 
# valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
# without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false

from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # validate the rows (borard = 9 X 9)
    for i in range(9):
        valid_row = set()
        for j in range(9):
            board_item = board[i][j]
            if board_item in valid_row:
                return False
            elif board_item != ".":
                valid_row.add(board_item)

    # validate the columns (borard = 9 X 9)
    for i in range(9):
        valid_col = set()
        for j in range(9):
            board_item = board[j][i]
            if board_item in valid_col:
                return False
            elif board_item != ".":
                valid_col.add(board_item)

    # validate individual boxes (3 X 3) on the board
    # -> identify the start positions
    all_starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]
    
    for i, j in all_starts:
        valid_board = set()
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                board_item = board[row][col]
                if board_item in valid_board:
                    return False
                elif board_item != ".":
                    valid_board.add(board_item)

    return True

# Neetcode (Bitmask)
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [0] * 9
#         cols = [0] * 9
#         squares = [0] * 9

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
                
#                 val = int(board[r][c]) - 1
#                 if (1 << val) & rows[r]:
#                     return False
#                 if (1 << val) & cols[c]:
#                     return False
#                 if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
#                     return False
                    
#                 rows[r] |= (1 << val)
#                 cols[c] |= (1 << val)
#                 squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

#         return True
    
board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

# board = [["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#         [".","9","1",".",".",".",".",".","3"],
#         ["5",".",".",".","6",".",".",".","4"],
#         [".",".",".","8",".","3",".",".","5"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".",".",".",".",".",".","2",".","."],
#         [".",".",".","4","1","9",".",".","8"],
#         [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))