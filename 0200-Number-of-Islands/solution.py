def flood_fill(board, x, y):
    if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
        return
    if board[x][y] != '1':
        return

    board[x][y] = '0'

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
        # what gives the amortized constant time complexity.
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
    def numIslands(self, grid):
        # SOLUTION 1 - Recursive Flood Fill Algorithm
        # O(n) Time, O(1) Space

        # The recursion only visits cells that are 1's and then changes them to water.
        # Therefore, a piece of land will not be revisted by subsequent recusive calls.
        # Hence O(n) Time

        # count = 0

        # if not grid:
        #     return count

        # rows, cols = len(grid), len(grid[0])

        # for x in range(rows):
        #     for y in range(cols):
        #         if grid[x][y] == '1':  # Land
        #             count += 1
        #             # Replace all connecting land with water
        #             flood_fill(grid, x, y)

        # return count

        # SOLUTION 2 - Union Find
        # We can union all the lands together and then count the number of sets
        # that are land (i.e the numvber of islands)

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        uf = UnionFind(rows*cols)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    next = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                    for i, j in next:
                        if i < 0 or j < 0 or i == rows or j == cols:
                            continue
                        if grid[i][j] == '1':
                            uf.unify(x*cols+y, i*cols+j)

        islands = set()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    islands.add(uf.find(x*cols+y))

        return len(islands)

