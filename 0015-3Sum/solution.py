class Solution:
    def threeSum(self, nums):
        # Solution 1 - Using 2 Sum
        # O(n^2) Time, O(n) Space

        # The idea is simple, choose a first number and then
        # perform 2 Sum to find two numbers that give the
        # remainding target.

        if not nums:
            return []

        nums.sort()                             # To remove duplicates easily
        target, n, res = 0, len(nums), set()    # Given target is 0
        m = nums[-1]                            # Largest number in array

        for i in range(n-2):
            a, seen = nums[i], set()
            # Impossibilities
            if a > target: break
            if a + 2*m < target: continue
            for k in range(i+1, n):
                c = nums[k]
                b = target - (a + c)
                if b in seen:
                    res.add((a, b, c))
                else:
                    seen.add(c)
        return list(res)

