class Solution:
    def spiralOrder(self, matrix):
        # Solution 1 - Top, Bottom, Left, Right
        # O(mn) Time, O(mn) Space

        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, cols-1, 0, rows-1
        res, count = [], rows * cols

        while len(res) < count:
            if top <= bottom:
                for j in range(left, right+1):
                    res.append(matrix[top][j])
                top += 1
            if right >= left:
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
            if bottom >= top:
                for j in range(right, left-1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

