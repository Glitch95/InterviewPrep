class Solution:
    def isIsomorphic(self, s, t):
        # We will iterate over both strings in lockstep.
        # Creating mapping of elements in string 1 to elements in string 2
        # If we encounter a new mapping, and either of its elements
        # have already been mapped, we return false.

        map, seen = {}, set()
        
        for x, y in zip(s, t):
            if x in map:
                if map[x] != y:
                    return False
            else:
                if y in seen:
                    return False
                map[x] = y
                seen.add(y)
        return True

