from collections import defaultdict, deque

def dfs(airport, graph, route):
    while graph[airport]:
        # Once we use a ticket we can't we it again so we remove (pop) it
        next_city = graph[airport].popleft() # popLEFT to maintain lexical order
        dfs(next_city, graph, route)
    route.appendleft(airport)

class Solution:
    def findItinerary(self, tickets):
        # SOLUTION 1 - Topological Sort

        # The key idea is to build up the route backwards starting
        # from the airport with no outgoing edges.

        # If n is the number of tickets
        # O(n) Time, O(n) Space

        graph = defaultdict(deque)
        for start, end in sorted(tickets):    # Sorted to resolve lexical order
            graph[start].append(end)

        route = deque()
        dfs('JFK', graph, route)    # We know the itinerary bigins at JFK
        return route

