from collections import Counter

class Solution:
    def frequencySort(self, s):
        # Get a count of the characters and sort in descending order by count
        counter = sorted(Counter(s).items(), key=lambda x:x[1], reverse=True)
        return ''.join([char * count for char, count in counter])

