class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Solution 1 - Greedy Approach
        # Time O(nlogn), Space O(1)

        # The key idea is to sort the intervals by their end time.
        # Remove intervals whose start time overlaps with the end time
        # of the previous interval.

        if not intervals or len(intervals) < 2:
            return 0

        intervals.sort(key = lambda x : x[1])   # Sort the intervals by end time

        n, last_valid_idx, remove_count = len(intervals), 0, 0

        for i in range(1, n):
            if intervals[i][0] < intervals[last_valid_idx][1]:
                remove_count += 1
            else:
                last_valid_idx = i

        return remove_count

