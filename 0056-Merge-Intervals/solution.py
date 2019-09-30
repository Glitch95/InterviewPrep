class Solution:
    def merge(self, intervals):
        # Solution 1 - Stack and Sorting
        # O(nlogn) Time, O(n) Space

        if not intervals:
            return []

        intervals.sort()        # Sort intervals by start value

        n, stack = len(intervals), [intervals[0]]

        for i in range(1, n):
            curr_start, curr_end = intervals[i]
            prev_start, prev_end = stack[-1]

            if curr_start <= prev_end:
                stack.pop()
                stack.append([prev_start, max(prev_end, curr_end)])
            else:
                stack.append([curr_start, curr_end])

        return stack

