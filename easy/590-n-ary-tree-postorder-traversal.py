"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        r = []
        if root==None:
            return r
        for c in root.children:
            r += self.postorder(c)
        r.append(root.val)
        return r