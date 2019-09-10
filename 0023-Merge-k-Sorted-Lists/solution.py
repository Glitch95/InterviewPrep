# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heapify, heappush, heappop

class Node:
    """ Wrapper class to enable comparing nodes """
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists):
        # The idea is simple, we will keep a min heap (of size k) of the first nodes of each list.
        # We pop the min node from the heap and push the next node in the list back on the heap.
        # We add the popped node to the merge list.
        
        head = tail = ListNode(None)
        
        heap = [Node(node) for node in lists if node]
        heapify(heap)
        
        while heap:
            node = (heappop(heap)).node
            if node.next:
                heappush(heap, Node(node.next))
            tail.next = node
            tail = tail.next
        
        return head.next

