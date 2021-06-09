"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root:
            n = 1 + max(self.maxDepth(child) for child in root.children) if root.children else 0
            return n
        else:
            return 0