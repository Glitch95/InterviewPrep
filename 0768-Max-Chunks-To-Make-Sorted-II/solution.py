class Solution:
    def maxChunksToSorted(self, arr):
        # Solution 1 - Dynamic Programming
        # O(n) Time, O(n) Space

        # For this problem, notice that we’re able to separate numbers into
        # different chunks when all the numbers we’ve evaluated are at
        # smaller than or equal to the smallest number in the set of numbers
        # we haven’t visited yet.

        # [2,1,4,4,3] -->  [2, 1], [4, 4, 3]
        # Since 2 and 1 are both smaller than 3.

        # Get the minimum of the numbers to the right
        n = len(arr)
        right_min = [float('inf')] * n  # Min to the right
        for i in range(n-2, -1, -1):
            right_min[i] = min(arr[i+1], right_min[i+1])

        curr_max, count = float('-inf'), 0
        for i in range(n):
            curr_max = max(curr_max, arr[i])
            if curr_max <= right_min[i]:
                count += 1
        return count

