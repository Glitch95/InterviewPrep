class Solution:
    def searchInsert(self, nums, target):
        # Solution 1 - Binary Search
        # O(logn) Time, O(1) Space
        
        # In short, we are trying to find the index of the first element in the array
        # that is greater than target.
        # It is important that we run the search even when the 2 pointers are equal
        # so that left and right will corss over. Hence while left <= right.
        # Once the left and right pointers cross, the left pointer will be where
        # the missing element would have been if it was inserted in the array.
        
        # To understand this, consider the case where the search is in 
        # the penultimate step, both left and right and mid will be pointing
        # to the same index. Everything to the left of left is smaller than target and 
        # everything to the right of right is larger than target.
        # Now we just need to decide whether the last element is smaller or larger than
        # target. If it is smaller then left moves to mid+1 and is at the index of the
        # first element larger than target.
        # If it is larger than target, right moves to mid-1 and left remain at the current
        # index which is the first element larger than the target.
        # Hence we return left if the element is not in the array.
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        return left
 
