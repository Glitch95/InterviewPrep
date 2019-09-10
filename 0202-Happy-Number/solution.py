class Solution:
    def isHappy(self, n):
        # We will repeatedly perform the operation to convert the number into a happy number
        # Making sure that we keep track of the numbers encountered along the way,
        # so that we can detect if there is a cycle (i.e we will never get to 1)
        # -- meaning that the number is not happy.
        
        seen = set()
        seen.add(n)
        while n != 1:
            n = sum([int(x)**2 for x in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        return True

