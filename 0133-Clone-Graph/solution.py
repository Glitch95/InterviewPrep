"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

def dfs(start, clone):
    if start not in clone:
        clone[start] = Node(start.val, [])

    for neighbor in start.neighbors:
        if neighbor not in clone:
            clone[neighbor] = Node(neighbor.val, [])
            dfs(neighbor, clone)
        clone[start].neighbors.append(clone[neighbor])

    return clone[start]

class Solution:
    def cloneGraph(self, node):
        # The idea is simple, we traverse the graph building a map
        # between the original nodes. We can then use this map
        # to link the cloned nodes in the same structure as the
        # original graph.

        # SOLUTION 1 - Recursive Depth First Traversal
        # O(n) Time, O(n) Space

        # return dfs(node, {})

        # SOLUTION 2 - Iterative Depth First Traversal
        # O(n) Time, O(n) Space

        # clone, stack = {}, [node]
        # clone[node] = Node(node.val, [])

        # while stack:
        #     vertex = stack.pop()

        #     for neighbor in vertex.neighbors:
        #         if neighbor not in clone:   # Clone represents the visited set of nodes
        #             clone[neighbor] = Node(neighbor.val, [])
        #             stack.append(neighbor)
        #         clone[vertex].neighbors.append(clone[neighbor])

        # return clone[node]

        # SOLUTION 3 - Iterative Breadth First Traversal
        # O(n) Time, O(n) Space

        from collections import deque

        clone, queue = {}, deque()
        queue.append(node)
        clone[node] = Node(node.val, [])

        while queue:
            vertex = queue.popleft()

            for neighbor in vertex.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clone[vertex].neighbors.append(clone[neighbor])

        return clone[node]

