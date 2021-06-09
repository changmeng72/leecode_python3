# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    v = None
    def isUnivalTree(self, root: TreeNode) -> bool:
            
        if root==None :
            return True
        if not self.v:
            self.v = root.val
        
        return  root.val == self.v and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            