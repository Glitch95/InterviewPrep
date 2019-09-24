from collections import defaultdict

def has_cycle(graph, start_node, visiting, visited):
    if start_node in visiting:
        return True

    visiting.add(start_node)

    if start_node in graph:
        for neighbor in graph[start_node]:
            if neighbor not in visited:
                if has_cycle(graph, neighbor, visiting, visited):
                    return True

    visiting.remove(start_node)
    visited.add(start_node)

    return False

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Solution 1 - Depth First Search
        # O(n) Time, O(n) Space

        # The key idea is to build a graph of teh courses and prerequisites
        # If there is a cycle in the graph then it is not possible to
        # finish all the courses.

        graph = defaultdict(set)
        for start, end in prerequisites:
            graph[start].add(end)

        # Detect cycle using dfs
        visited, visiting = set(), set()
        for node in graph:
            if has_cycle(graph, node, visiting, visited):
                return False
        return True

