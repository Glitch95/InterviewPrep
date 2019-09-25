def getIndex(row, col, num_cols):
    return row * num_cols + col

def getRowCol(index, num_cols):
    return index // num_cols, index % num_cols

class Solution:
    def searchMatrix(self, matrix, target):
        # Solution 1 - Binary Search
        # If m and n are the dimensions of the matrix:
        # O(log(mn)) Time, O(1) Space

        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])

        start, end = 0, getIndex(rows-1, cols-1, cols)

        while start <= end:
            mid = (start + end) // 2
            r, c = getRowCol(mid, cols)

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                start = mid + 1
            else:
                end = mid -1

        return False

