def dfs(start, graph, color):
    # We arbitrarily chose 0 as the starting color (set) for top level nodes
    # i.e. the first node visited in a part of the graph that
    # is disjoint from the rest.
    if start not in color:
        color[start] = 0

    for neighbor in graph[start]:
        if neighbor in color:
            if color[neighbor] == color[start]:
                return False
        else:
            color[neighbor] = 1 - color[start]  # Flips between 1 and 0
            if not dfs(neighbor, graph, color):
                return False
    return True

def dfs_iter(start, graph, color):
    # We arbitrarily chose 0 as the starting color (set) for top level nodes
    # i.e. the first node visited in a part of the graph that
    # is disjoint from the rest.
    if start not in color:
        color[start] = 0

    stack = [start]

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor in color:
                if color[node] == color[neighbor]:
                    return False
            else:
                color[neighbor] = 1 - color[node]     # Flips between 1 and 0
                stack.append(neighbor)
    return True


class Solution:
    def isBipartite(self, graph):
        # The idea is to traverse the graph using dfs
        # adding each vertex of an edge to a separate set
        # (in this code we call the set a color)
        # We use 0 and 1, because we can easily flip
        # between them using color = 1 - color

        # SOLUTION 1 - Recursive Depth First Search
        # O(n) Time, O(n) Space

        # color = {}    # Represents the set of visited nodes as well.
        # for node in range(len(graph)):
        #     if node not in color: # We only run dfs on nodes that don't have a color (set)
        #         if not dfs(node, graph, color):
        #             return False
        # return True

        # SOLUTION 2 - Iterative Depth First Search
        # O(n) Time, O(n) Space

        color= {}   # Represents the set of visited nodes as well.
        for node in range(len(graph)):
            if node not in color:   # We only run dfs on nodes that don't have a color (set)
                if not dfs_iter(node, graph, color):
                    return False
        return True

