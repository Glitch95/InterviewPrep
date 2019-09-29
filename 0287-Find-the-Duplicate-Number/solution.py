class Solution:
    def findDuplicate(self, nums):
        # If we weren't constrained to O(1) Space, we
        # could easily find the answer in lnear time and
        # space by using a set.

        # Solution 1 - Floyd's Cycle Detection Algorithm
        # O(n) Time, O(1) Space

        # If we interpret nums such that for each pair of index i and value v_i,
        # the "next" value v_j is at index v_i, we can reduce this problem to
        # cycle detection.

        # First off, we can easily show that the constraints of the problem imply
        # that a cycle must exist. Because each number in nums is between 1 and n,
        # it will necessarily point to an index that exists. Therefore, the list
        # can be traversed infinitely, which implies that there is a cycle.
        # Additionally, because 0 cannot appear as a value in nums, nums[0] cannot
        # be part of the cycle. Therefore, traversing the array in this manner from
        # nums[0] is equivalent to traversing a cyclic linked list.

        slow = fast = nums[0]   # Important that  both start at nums[0]

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return fast

