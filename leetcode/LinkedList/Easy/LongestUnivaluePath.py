"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        self.longestV = 0

        def longest(root):
            if not root:
                return 0
            leftP, rightP= longest(root.left), longest(root.right)

            left = (leftP+1) if root.left and root.val ==root.left.val else 0
            right = (rightP+1) if root.left and root.val ==root.right.val else 0

            self.longestV = max(self.longestV, (left+right))

            return max(left, right)
        longest(root)

        return self.longestV
