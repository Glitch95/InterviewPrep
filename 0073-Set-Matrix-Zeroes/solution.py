class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Solution 1 - Hash Set
        # IF m and n are the dimensions of the matrix.
        # O(mn) Time, O(n+m)Space

        # The key idea is to go through the matrix and
        # record the rows and cols where 0s are encountered

        if not matrix:
            return

        rows, cols = len(matrix), len(matrix[0])

        zero_rows, zero_cols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

