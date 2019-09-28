from math import ceil

class Solution:
    def maximumGap(self, nums):
        # Solution 1 - Bucket Sort
        # O(n) Time, O(n) Space

        # Suppose there are N elements in the array, hen the
        # maximum gap will be at least as large as
        # ceiling[(max - min ) / (N - 1)].

        # So if we make the buckets smaller than the maximum gap,
        # any gaps within the same bucket is not the amount we only
        # have to at the inter-bucket gaps.

        # As of such, we only need to store the max and min values
        # in each bucket.

        if not nums:
            return 0

        n = len(nums)

        if n < 2:
            return 0

        min_n, max_n = min(nums), max(nums)

        # There are only n-1 gaps between n numbers (at least 1 bucket will be empty)
        bucket_min, bucket_max = [float('inf')] * (n-1), [float('-inf')] * (n-1)

        bucket_size = ceil((max_n - min_n) / (n-1))  # The minimum max gap possible

        # Put the numbers into the buckets
        for num in nums:
            if num == min_n or num == max_n:
                continue
            idx = (num - min_n) // bucket_size      # Index of the right position in the buckets
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)

        # Check the inter-bucket gaps to get the max gap
        max_gap, prev_max = float('-inf'), min_n

        print(bucket_min)
        print(bucket_max)

        for i in range(n-1):
            if bucket_min[i] == float('inf') and bucket_max[i] == float('-inf'):    # Empty bucket
                continue
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        max_gap = max(max_gap, max_n - prev_max);   # Update the final max value gap

        return max_gap

