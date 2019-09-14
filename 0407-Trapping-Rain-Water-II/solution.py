from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap):
        """ 
        WHY DYNAMIC PROGRAMMING WON'T WORK.
        
        It seems intuitive to extend the dp approach
        that we used for Trapping Water I to solve this
        problem. However, this will not work due to the
        fact that the water trapped above a bar is not
        only dependent on the max height to its left, right,
        up and down; but also on the height of the water
        that can be stored above the bars immediately
        adjacent to it.
        
        To visualize this, consider the following instance:
        
        Given elevation map:
        [[12,13,1,12],
        [13,4,13,12],
        [13,8,10,12],
        [12,13,12,12],
        [13,13,13,13]]

        The dp approach would give the following solution:
        [[0,0,0,0],
        [0,9,0,0],
        [0,4,2,0],
        [0,0,0,0],
        [0,0,0,0]]
        
        which gives 15 (9 + 4 + 2) units of trapped water,
        but the CORRECT answer is 14.
        
        The reason for this is:
        
        (2,1) will be able to hold a capacity of (12 - 8) = 4 units,
        as if we look in all 4 directions 12 is the minimum height barrier
        for index (2,1). So effective height at (2,1) will be 12.
        Due to this, the minimum height barrier surrounding (1,1) will now be 12, 
        NOT 13. Hence, effective water capacity at (1,1) would now be (12 - 4) = 8 units.

        Total capacity = (1,1) : 8 units, + (2,1) : 4 units + (2,2) : 2 units = 14 units
        
        The reason the dynamic programming approach won't work here is because
        the minimum boundary for a cell keeps on changing based on the minimum
        boundary of adjacent cells.
        
        
        SOLUTION - Using a Min Heap.
        If the size of the elevation map is m x n:
        Time O((mxn)log(2(m+n))) = O((mxn)log(m+n))
        Space O(2(m+n)) = O(m+n)
        
        We know that the cells at the boundaries of the elevation map
        won't trap any water, and therefore their minimum bounday won't 
        change.
        
        If we start with the boundary cell with minimum height and 
        record the water that would be stored in its adjacent cells
        (i.e left, right, up, down), due to it being the minimum boundary 
        of those cells. 
        
        Then we replace the height of the adjacent cells with the height of
        water stored them + thier original height. If no water is trapped above
        the adjacent cell we use its original height.
        
        If we repeatedly take the cell with minimum height and 
        perform the above steps, making sure not to re-visit cells we already 
        used; we can compute the total trapped water.
        """
        
        if not heightMap:
            return 0
        
        trapped_water, min_heap, seen, rows, cols = 0, [], set(), len(heightMap), len(heightMap[0])
        
        # Add the boundary columns to min heap
        for i in range(rows):
            heappush(min_heap, (heightMap[i][0], i, 0))
            seen.add((i, 0))
            heappush(min_heap, (heightMap[i][cols-1], i, cols-1))
            seen.add((i, cols-1))
    
        # Add the boundary rows to min heap
        for j in range(cols):
            heappush(min_heap, (heightMap[0][j], 0, j))
            seen.add((0, j))
            heappush(min_heap, (heightMap[rows-1][j], rows-1, j))
            seen.add((rows-1, j))
        
        while min_heap:
            height, row, col = heappop(min_heap)
            adjacent_cells = [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]
            
            for r, c in adjacent_cells:
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in seen:
                    next_height = heightMap[r][c]
                    trapped_water += max(0, height-next_height)
                    heappush(min_heap, (max(height, next_height), r, c))
                    seen.add((r, c))
            
        return trapped_water

