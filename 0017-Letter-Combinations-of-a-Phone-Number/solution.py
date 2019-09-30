class Solution:
    def letterCombinations(self, digits):
        # Solution 1 - Iterative Backtracking
        # O(n^k) Time - where k is the average number of letters a digit
        # maps to and n is the total number of digits in the string.
        # O(n) Space

        if not digits:
            return []

        map = {
            '2': set('abc'),
            '3': set('def'),
            '4': set('ghi'),
            '5': set('jkl'),
            '6': set('mno'),
            '7': set('pqrs'),
            '8': set('tuv'),
            '9': set('wxyz')
        }

        combinations, new_combinations = [''], []

        for digit in digits:
            for combination in combinations:
                for letter in map[digit]:
                    new_combinations.append(combination + letter)
            combinations, new_combinations = new_combinations, []

        return combinations

