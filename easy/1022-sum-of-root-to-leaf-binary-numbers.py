# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def rootToLeaf(self,root: TreeNode, p: int) -> int:
            if root.left==None and root.right==None:
                self.r += (p<<1|root.val)
            else:
                if root.left!=None:
                    self.rootToLeaf(root.left, p<<1|root.val)
                if root.right!=None:
                    self.rootToLeaf(root.right, p<<1|root.val)
        
    
   
            
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.r = 0
        self.rootToLeaf(root,0)
        return self.r
                    