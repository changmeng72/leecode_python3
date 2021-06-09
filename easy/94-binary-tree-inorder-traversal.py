# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack = []
        res = []
        
        if not root:
            return []
        if root.right:
            stack.append((root.right,0))
        if root:
            stack.append((root,1))
        if root.left:
             stack.append((root.left,0))
        while stack:
            node = stack.pop()
            if node[1]==0:
                if node[0].right:
                    stack.append((node[0].right,0))
                if node[0].left:
                    stack.append((node[0],1))
                    stack.append((node[0].left,0))
                else:
                    res.append(node[0].val)
            else:
                res.append(node[0].val)
                
        return res
                         
                         
            
        
        
        
        """ recursive
        if not root:
            return []
        res =[]
        if(root.left):
            res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        if(root.right):
            res.extend(self.inorderTraversal(root.right))
        return res
        """
        