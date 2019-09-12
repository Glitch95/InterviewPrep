from random import randint
from math import sqrt

def distance(point):
    """Returns the distance of the point from the origin"""
    return sqrt(point[0]**2 + point[1]**2)

def partition(arr, p, r):
    """ Partitions arr[p:r+1] and returns the pivot index """
    x = arr[r]  # pivot
    i = p - 1  # All elements before index i are <= pivot (WRT distance from origin)
    # Exclude the last element (pivot) hence [p ... r-1]
    for j in range(p, r):
        if distance(arr[j]) <= distance(x):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # a[i+1] is the first element greater than the pivot value
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

def rand_partition(arr, p, r):
    # Make a random element the pivot before partitioning
    # to avoid the degenerate case.
    i = randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)


def randomized_quickselect(arr, i, p=0, r=None):
    """Returns the ith element of the array in expected O(n) time."""
    if r is None:
        r = len(arr) - 1

    if i < 1 or i > r - p + 1:
        raise ValueError

    if p == r:
        return arr[p]

    q = rand_partition(arr, p, r)

    k = q - p + 1  # The kth element (We know what it is)

    if i == k:
        return arr[q]
    elif i < k:
        return randomized_quickselect(arr, i, p, q - 1)
    else:
        return randomized_quickselect(arr, i - k, q + 1, r)

class Solution:
    def kClosest(self, points, K):
        # The naive approach is to maintain a min heap (by distance from the origin)
        # of size k.
        # However this approach yields an O(nlogk) time complexity.
        
        # A more efficient approach is to leverage the fact that the
        # k closest points can be returned in any order.
        # Therefore, we can use the randomized quick select algorithm
        # that we learned from order statistics, which runs in 
        # expected O(n) time.
        
        _ = randomized_quickselect(points, K)
        return points[:K]

