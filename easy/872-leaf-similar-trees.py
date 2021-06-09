# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leafgenerator(self,root:TreeNode):
        stack = []        
        stack.append(root)
        
        while stack:
            r = stack.pop()
            if(r.right):
                stack.append(r.right)
            if(r.left):
                stack.append(r.left) 
            if r.left==None and r.right==None:
                yield r.val
    
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        root1_leaves =  self.leafgenerator(root1)
        root2_leaves =  self.leafgenerator(root2)
        
        while True:
            leaf1 =next( root1_leaves,None)
            leaf2 =next( root2_leaves,None)
            
            if(leaf1!=leaf2):
                return False
            if(leaf1==None and leaf2==None):
                return True
        return True
            
"""
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaves(root):
            if root is not None:
                if root.left is None and root.right is None:
                    yield root.val
                else:
                    yield from leaves(root.left)
                    yield from leaves(root.right)
        return list(leaves(root1)) == list(leaves(root2))
"""