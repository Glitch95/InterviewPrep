class Solution:
    def myPow(self, x, n):
        # Solution 1 - Recursive Implementation
        # O(logn) Time, O(1) Space
        # The idea is that pow(x, n) = pow(x, n/2) * pow (x, n/2)

        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:     # Base case for negative powers
            return 1 / x

        half = n//2
        return pow(x, half) * pow(x, n-half)

