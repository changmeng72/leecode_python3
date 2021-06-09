# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        if root==None:
            return []
        
        #iterative:
        stack = []
        stack.append(root)
        
        while stack:
            n = stack.pop()
            if n.left:
                t = n.left
                n.left=None
                stack.append(n)
                stack.append(t)
            elif n.right:
                t = n.right
                n.right=None
                stack.append(n)
                stack.append(t)
            else:
                ans.append(n.val)
        return ans
                
            
        
        """
        #recursive:
        if root.left !=None:
            ans += self.postorderTraversal(root.left)
        if root.right!=None:
            ans += self.postorderTraversal(root.right)
        if root!=None:
            ans += [root.val]
        return ans
         """   
        