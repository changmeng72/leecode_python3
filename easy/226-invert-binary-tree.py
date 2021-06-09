# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = [root]
        if root:
            while q:
                r = q.pop()
                t = r.left
                r.left = r.right
                r.right = t
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
        return root
        
        
        """
        if root:
            t = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = t
            return root
        return None
        """
        