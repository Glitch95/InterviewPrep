from heapq import heapify, heappush, heappop

class Solution:
    def smallestRange(self, nums):
        """The approach is to start off with the first elements of the
        list, we then repeatedly remove the min element in that 'range'
        and add the successor from its list.
        We can use a min heap to easily find which element to increase.
        
        Time O(nlogk)
        """
        
        # Store the first element in each list in a min heap
        # We need to store the number, corresponding row for that number,
        # and index in row for that number
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapify(heap) # this creates the heap

        # Best interval so far with the minimum set to negative infinity 
        # and the maximum set to positive infinity
        best_interval = (float("-inf"), float("inf")) 

        # Go through all the rows to get the current highest number
        curr_max = max(row[0] for row in nums) 

        while heap:
            # Removes the smallest element from the heap
            curr_min, row_num, row_index = heapq.heappop(heap) 

            if curr_max - curr_min < best_interval[1] - best_interval[0]:
                best_interval = (curr_min, curr_max)

            # If we exhaust any of the lists, we're done.
            if row_index + 1 == len(nums[row_num]):
                return best_interval

            new_elem = nums[row_num][row_index+1]
            curr_max = max(curr_max, new_elem)
            heappush(heap, (new_elem, row_num, row_index+1))

