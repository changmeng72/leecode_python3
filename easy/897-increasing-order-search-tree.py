# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = root
        if root.left:
            l =  self.increasingBST(root.left)
            t = l
            while t.right!=None:
                t = t.right
            t.right = root
            root.left = None
        
        if root.right:
            root.right = self.increasingBST(root.right)
        
        return l
            