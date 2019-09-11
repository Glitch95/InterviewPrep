from collections import Counter
from heapq import heappop, heapify

class Solution:
    def topKFrequent(self, words, k):
        # We create a dictionary of the words and their frequencies.
        # Using the dict we create a max heap
        # and return the top k elements in the heap
        counter = Counter(words)
        heap = [(-count, word) for word, count in counter.items()]  # -count -> max heap
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

