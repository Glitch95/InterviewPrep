class Solution:
    def isValidSudoku(self, board):
        # The idea is iterate over the board, keeping track of
        # what we've seen and where we saw it 
        # (i.e. in which row, col and box).
        # If we ecnounter a number we have already seen in the 
        # current row, col, or box we return False.

        rows, cols, boxes = [[set() for _ in range(9)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                
                val = int(board[row][col])
                
                if val in rows[row]:
                    return False
                if val in cols[col]:
                    return False
                box = (3 * (row // 3)) + (col // 3)
                if val in boxes[box]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                boxes[box].add(val)
        
        return True

