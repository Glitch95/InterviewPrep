from bisect import bisect_left

class MedianFinder:
    """ The idea is to maintain a sorted list, 
    every time we add an element which we can
    accomplish using insertion sort."""
    
    # Time complexity
    # Adding a number takes O(n) time
    # i.e log(n) to find the insert position
    # and O(n) to do the actual insert.
    # O(n) + O(logn) = O(n)
    # Finding the median takes constant O(1) time.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sorted_data = []
        
    def addNum(self, num):
        self.sorted_data.insert(bisect_left(self.sorted_data, num), num)

    def findMedian(self):
        # Median is the middle value in an ordered integer list. 
        # If the size of the list is even, there is no middle value. 
        # So the median is the mean of the two middle value.
        data, n = self.sorted_data, len(self.sorted_data)
        return data[n//2] if n & 1 else (data[n//2-1] + data[n//2]) * 0.5

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

