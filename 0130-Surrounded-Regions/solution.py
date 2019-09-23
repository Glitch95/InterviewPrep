def flood_fill(board, x, y):
    if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
        return
    if board[x][y] != 'O':
        return

    board[x][y] = '-'

    flood_fill(board, x-1, y)
    flood_fill(board, x+1, y)
    flood_fill(board, x, y-1)
    flood_fill(board, x, y+1)

# ------------------ UnionFind / Disjoint Set Data Structure -------------------------
class UnionFind:
    def __init__(self, size):
        """ Initializes the data structure. """
        # Each component is initially of size 1
        self.comp_size = [1] * size
        # Each component is initially its own parent/root (self loop)
        self.id = [i for i in range(size)]

    def find(self, p):
        """ Finds which component/set 'p' belongs to in amortized constant time. """

        # Find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # Compress the path leading back to the root
        # This operation is called "path compression" and is
        # waht gives the amortized constant time complexity.
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next

        return root

    def unify(self, p, q):
        """ Unify the components/sets containing p/q. """
        root1, root2 = self.find(p), self.find(q)

        # If the elements are already in the same set
        if root1 == root2:
            return

        # Merge the smaller component/set into the larger one.
        if self.comp_size[root1] < self.comp_size[root2]:
            self.comp_size[root2] += self.comp_size[root1]
            self.id[root1] = root2
        else:
            self.comp_size[root1] += self.comp_size[root2]
            self.id[root2] = root1

    def connected(self, p, q):
        """ Returns whether or not the components 'p' and 'q'
        are in the same component/set. """
        return self.find(p) == self.find(q)
# -------------------------------------------------------------------------------

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # SOLUTION 1 - Recursive Flood Fill Algorithm (DFS)

        # O(n) Time, O(1) Space
        # The recursion only visits cells with an 'O' and then
        # changes the value to '-'. Therefore the same 'O' will
        # not be visited again by other recursive calls.
        # Hence, time complexity is O(n)

        # Imagine O's are like water, we flood (connect) all the O's
        # that are connected to a boundary.
        # We then capture all the other O's replacing them with X's
        # and replace the flooded positions with O's.

        # Let n, m be the dimensions of the board
        # O(mn) Time, O(mn) Space - Depth of Deepest Recursion

        # if not board:
        #     return

        # rows, cols = len(board), len(board[0])

        # for x in range(rows):
        #     flood_fill(board, x, 0)
        #     flood_fill(board, x, cols-1)

        # for y in range(cols):
        #     flood_fill(board, 0, y)
        #     flood_fill(board, rows-1, y)

        # for x in range(rows):
        #     for y in range(cols):
        #         if board[x][y] == 'O':
        #             board[x][y] = 'X'
        #         elif board[x][y] == '-':
        #             board[x][y] = 'O'

        # SOLUTION 2 - Union Find

        # O(n) Time, O(n) Space
        # Union Find opeartions take O(1) amortized time.
        # Hence, time complexity is O(n)

        # The mapping between nodes and numbers will be implicitly derived
        # from the  row and col of the cell.
        # We will also include a dummy node to which we will connect
        # all 'O's that cannot be captured.

        if not board:
            return

        rows, cols = len(board), len(board[0])

        uf = UnionFind(rows*cols + 1) # +1 for the dummy node
        dummy = rows * cols

        for x in range(rows):
            for y  in range(cols):
                # Connect 'O's on the boundary to the dummy node
                if x == 0 or y == 0 or x == rows-1 or y == cols-1 and board[x][y] == 'O':
                    uf.unify(dummy, x*cols+y)
                # Connect internal 'O's to neighboring 'O's
                elif board[x][y] == 'O':
                    next = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for i, j in next:
                        if board[i][j] == 'O':
                            uf.unify(x*cols+y, i*cols+j)

        # No need for boundary cases since we're not changing the 'O's there.
        for x in range(1, rows-1):
            for y  in range(1, cols):
                # If an'O' is not connected to the dummy node it is captured
                if board[x][y] == 'O' and not uf.connected(x*cols+y, dummy):
                    board[x][y] = 'X'

