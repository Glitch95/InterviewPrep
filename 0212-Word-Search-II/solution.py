from collections import defaultdict

# -------------- Tire Data Structure ------------------
class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for char in word:
            curr_node =  curr_node.children[char]
        curr_node.end = True
# -----------------------------------------------------

def dfs(board, x, y, trie_node, curr_word, visited, found):
    # If this is a word in the dictionary?
    if trie_node.end:
        found.append(''.join(curr_word))
        trie_node.end = False       # To avoid duplicates
    # Check for invalid (out of bounds) indices.
    if x < 0 or y < 0 or x == len(board) or y == len(board[0]):
        return
    # The same letter cell may not be used more than once in a word
    if (x,y) in visited:
        return

    curr_char = board[x][y]

    # Prune the search if curr char is not in any word
    if curr_char not in trie_node.children:
        return

    # Update the trie node to the corresponding child node
    trie_node = trie_node.children[curr_char]

    visited.add((x,y))      # Update the state (for backtracking)
    curr_word.append(curr_char)

    dfs(board, x-1, y, trie_node, curr_word, visited, found)
    dfs(board, x+1, y, trie_node, curr_word, visited, found)
    dfs(board, x, y-1, trie_node, curr_word, visited, found)
    dfs(board, x, y+1, trie_node, curr_word, visited, found)

    curr_word.pop()
    visited.remove((x,y))   # Restore the state (for backtracking)

class Solution:
    def findWords(self, board, words):
        # The intuitive approach is to look for every word in the dictionary
        # on the board, like we did in Word Search I.

        # However, this approach is too slow as the search space is too large.
        # We can prune the serach space when the current character is not in any
        # word. To know if the current character is in any word at
        # we can use the Trie data structure.

        trie = Trie()
        for word in words:
            trie.insert(word)

        curr_word, visited, found = [], set(), []
        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(board, x, y, trie.root, curr_word, visited, found)
        return found

