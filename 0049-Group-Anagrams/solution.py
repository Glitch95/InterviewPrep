from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):        
        # Solution 1 - Sorting
        # O(nlogn) Time, O(n) Space
        
        # groups = defaultdict(list)
        # for s in strs:
        #     groups[''.join(sorted(s))].append(s)    # Sorted always returns a list
        # return groups.values()
        
        # Solution 2 - Hash Map
        # O(n) Time, O(n) Space
        
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            groups[tuple(count)].append(s)  # mutable list cannot be a dict key
        return groups.values()         
 
