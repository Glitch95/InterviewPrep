from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Solution 1 - Iterative Level Order (Breadth First) Traversal
    # O(n) Time, O(n) Space

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''

        queue, result = deque(), []
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('null')

        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        if data == '':
            return None

        vals = data.split(',')

        queue, root = deque(), TreeNode(int(vals[0]))
        queue.append(root)

        i, n = 1, len(vals)
        while i < n:
            node = queue.popleft()
            val = vals[i]
            if val == 'null':
                node.left = None
            else:
                node.left = TreeNode(int(val))
                queue.append(node.left)
            i += 1

            if i < n:
                val = vals[i]
                if val == 'null':
                    node.right = None
                else:
                    node.right = TreeNode(int(val))
                    queue.append(node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

