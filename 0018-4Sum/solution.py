class Solution:
    def fourSum(self, nums, target):
        # A typical k-sum problem. Time is N to the power of (k-1)
        # In this case, O(n^3)
        
        # We can sort the array to do some optimizations
        # Including:
        # 1. Not iterating form 0 to n-1 in each loop
        # 2. Short circuting if we know we are going down
        #    a dead end.
        
        # NOTE: This is essentially a backtracking problem,
        # however it is more intuitive and efficient to use
        # 3 loops, rather than a recursive backtracking 
        # template.
        
        if not nums:
            return []
        
        nums.sort()     # Sort the numbers
        n, m, result = len(nums), nums[-1], set()

        for i in range(n-3):
            a = nums[i]
            # Short circuit (Have we reached an impossibility?)
            if a + 3*m < target: continue
            if 4*a > target: break
            for j in range(i+1, n-2):
                b = nums[j]
                # Short circuit (Have we reached an impossibility?)
                if a + b + 2*m < target: continue
                if a + 3*b > target: break
                seen = set()
                for k in range(j+1, n):
                    d = nums[k]
                    c = target - (a + b + d)
                    if c in seen:                       
                        result.add((a, b, c, d))
                    else:
                        seen.add(d)
        return [[num for num in res] for res in result]

