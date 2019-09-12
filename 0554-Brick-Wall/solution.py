from collections import defaultdict

class Solution:
    def leastBricks(self, wall):
        # We are interested in the cumulative sum of brick lengths for each row.
        # We know when these cumulative sums match, we do not cut through those 
        # bricks at that point. Furthermore, we can ignore the last brick in 
        # every row since all rows are the same length and we cannot cut at the end.

        # We maintain the number of rows that have each cumulative sum amount, 
        # and can thus obtain the number of rows we are not cutting through for 
        # each place to cut. By subtracting this number from the total number of 
        # rows, we get the number of bricks that are cut through. We therefore
        # look for the cumulative sum with the most number of aligned bricks.
        
        counter = defaultdict(int)
        for row in wall:
            edge = 0
            for brick in row[:-1]:      # Ignore last brick in row
                edge += brick
                counter[edge] += 1
        return len(wall) - (0 if not counter else max(counter.values()))

