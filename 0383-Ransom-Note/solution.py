from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        # Solution 1 - Hash Map
        # O(n) Time, O(n) Space

        note_letters, magazine_letters = Counter(ransomNote), Counter(magazine)
        magazine_letters.subtract(note_letters)
        return all(count >= 0 for count in magazine_letters.values())

