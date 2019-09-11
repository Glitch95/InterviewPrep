from heapq import heapify, heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        # Time Complexity: O(klogk)
        # Basic idea: 
        # Use minHeap to keep track of next minimum pair sum, 
        # and we only need to maintain K possible candidates 
        # in the data structure.

        # Some observations: 
        # For every number in nums1, its best partner(yields min sum) 
        # always strats from nums2[0] since both arrays are sorted; 
        # And for a specific number in nums1, its next candidate sould be
        # itself + nums2[current_associated_index + 1], unless
        # the associated index is out of bounds.
        # To get the next candidate, we must store the index of
        # next element in nums2.

        # Method:
        # Frist, we take the first k elements of nums1 and pair them
        # with nums2[0] as the starting pairs.
        # So we have (0,0), (1,0), (2,0),.....(k-1,0) in the minHeap.
        # Each time we pop from the min heap, we add the pair to the results
        # and, we put the new pair with the associated index + 1 (candidate element)
        # on the heap.
        
        pairs = []
        
        if not nums1 or not nums2 or not k:
            return pairs
    
        n1, n2 = len(nums1), len(nums2)
        k = min(k, n1 * n2)     # Since we must return all possible pairs if k is too large

        min_heap = [(nums1[i] + nums2[0], [nums1[i], nums2[0]], 1) for i in range(min(n1, k))]
        heapify(min_heap)
        
        while k:
            _, pair, next = heappop(min_heap)
            pairs.append(pair)
            if next < n2:
                heappush(min_heap, (pair[0] + nums2[next], [pair[0], nums2[next]], next+1))
            k -= 1
        
        return pairs

