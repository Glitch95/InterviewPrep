def dfs(board, word, x, y, i, visited):
    """ i is the index of the next character in the word that we are searching for. """
    if i == len(word):
        return True
    if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
        return False
    if board[x][y] != word[i]:
        return False
    if (x,y) in visited:
        return False

    visited.add((x,y))      # Update the state (for backtracking)

    ret = dfs(board, word, x-1, y, i+1, visited) \
          or dfs(board, word, x+1, y, i+1, visited) \
          or dfs(board, word, x, y-1, i+1, visited) \
          or dfs(board, word, x, y+1, i+1, visited)

    visited.remove((x,y))   # Restore the state (for backtracking)

    return ret

class Solution:
    def exist(self, board, word):
        # SOLUTION 1 - Dfs and Backtracking
        # We perform dfs looking for the next character in the word.
        # We must ensure that we remove the current node from the
        # visited set when the recursion returns to the previous level.
        # This ensures that all posibilities are considered, and is the
        # backtracking part of the solution.

        # Let n, m be dimensions of the board
        # and l is the length of the word
        # O(n * m * l^4) Time, O(m * n) Space

        m, n, visited = len(board), len(board[0]), set()

        if len(word) > m * n:   # Sanity Check
            return False

        for x in range(m):
            for y in range(n):
                if dfs(board, word, x, y, 0, visited):
                    return True
        return False

