from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        # Solution 1
        # O(n) Time, O(n) Space
        
        # The idea is to remove leaf nodes one level at a time until there
        # are less than or equal to 2 nodes remaininig. The remaining nodes
        # will be roots for min height trees.
        # Leaf nodes are nodes that only belong to 1 edge.
        # i.e. their degree is 1
        
        if n == 1:  # If there is only 1 node in the graph.
            return [0]
        
        graph, degree, leaves = defaultdict(set), [0] * n, []
        
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            degree[a], degree[b] = degree[a] + 1, degree[b] + 1
                
        leaves = list(filter(lambda node: degree[node] == 1, range(n)))
                
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            while leaves:
                leaf = leaves.pop()
                
                for neighbor in graph[leaf]:
                    graph[neighbor].remove(leaf)
                    
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
                        
            leaves = new_leaves
        
        return leaves

