# Question
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
# You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
# You are given a helper function bool knows(a, b) which tells you whether A knows B.
# Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.
# Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party.

class Solution:
    def find_celeb2(n):
        """
        We can use the 2 Pointer Technique to solve this problem.
        O(n) Time, O(1) Space.

        In this solution, we compare pairs of people to see if one knows the other.
        We maintain two pointers (left and right) corresponding to people,
        initialized to the beginning and end of the list.
        We know if left knows right, then left cannot be the celebrity, so we increment left.
        We also know if left does not know right, then right cannot be the celebrity,
        so we decrement right. This continues until the pointers are the same.
        This is the only candidate celebrity, so we perform a final check to see if this
        candidate knows no one and everyone knows the candidate (since we don't do all
        checks while searching for the candidate).
        """
        left_idx, right_idx = 0, n - 1

        while left_idx < right_idx:
            if knows(left_idx, right_idx):
                left_idx += 1
            else:
                right_idx -= 1
        for idx in range(n):
            if idx == left_idx:
                continue
            if knows(left_idx, idx):
                return -1
            if not knows(idx, left_idx):
                return -1
        return left_idx
