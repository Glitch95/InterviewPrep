from collections import deque, defaultdict

def bfs(graph, start, end):
    queue, visited = deque([(start, 1)]), set([start])

    while queue:
        word, count = queue.popleft()

        for i in range(len(word)):
            key = word[:i] + '*' + word[i+1:]

            for neighbor in graph[key]:
                if neighbor == end:
                    return count + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, count+1))

    return 0    # Should never be reached

def visit_node(graph, queue, visited, other_visited):
    """ Helper function for bidirectional bfs. """
    word, count = queue.popleft()

    for i in range(len(word)):
        key = word[:i] + '*' + word[i+1:]

        for neighbor in graph[key]:
            # If the intermediate neighbor/word has already been visited from the
            # other parallel traversal this means we have found the answer.
            if neighbor in other_visited:
                return count + other_visited[neighbor]
            if neighbor not in visited:
                visited[neighbor] = count + 1
                queue.append((neighbor, count+1))

    return None

def bidirectional_bfs(graph, start, end):
    queue_start, queue_end = deque([(start, 1)]), deque([(end, 1)])
    visited_start, visited_end = {start: 1}, {end: 1}
    result = None

    # We do a birdirectional search starting one pointer from begin
    # word and one pointer from end word. Hopping one by one.
    while queue_start and queue_end:
        # One hop from begin word
        result = visit_node(graph, queue_start, visited_start, visited_end)
        if result:
            return result
        # One hop from end word
        result = visit_node(graph, queue_end, visited_end, visited_start)
        if result:
            return result

    return 0    # Should not be reached


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # Sanity checks
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        # Make a graph of the words in the list
        graph = defaultdict(list)
        n = len(beginWord)  # All words have the same length
        for word in wordList:
            for i in range(n):
                key = word[:i] + '*' + word[i+1:]
                graph[key].append(word)

        # SOLUTION 1 - Beadth First Search
        # If n is the number of word and k is the length of the word.
        # O(nk) Time - Fully connected graph
        # O(nk) Space

        # return bfs(graph, beginWord, endWord)

        # SOLUTION 2 - Bidirectional BFS
        # If n is the number of word and k is the length of the word.
        # O(nk) Time - Fully connected graph
        # O(nk) Space

        # The search space considered by BFS increases exponentially along with the number of levels.
        # Bidirectional BFS considerably cuts down on the search space and
        # hence reduces the time and space complexity.
        # Termination condition for bidirectional search is finding a word which is
        # already been seen by the parallel search.

        return bidirectional_bfs(graph, beginWord, endWord)

