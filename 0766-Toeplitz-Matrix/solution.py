class Solution:
    def isToeplitzMatrix(self, matrix):
        # Solution 1 - Hash Map
        # O(n) Time, O(n) Space

        # The key idea is to realize that 2 coordinates (r1, c1) and (r2, c2)
        # belong to the same diagonal if and only if (r1-c1) == (r2-c2).

        diagonals = {}

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in diagonals:
                    diagonals[r-c] = val
                elif diagonals[r-c] != val:
                    return False
        return True

