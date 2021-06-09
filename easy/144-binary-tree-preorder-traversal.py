# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        if root==None:
            return ans
        stack = [root]
        
        while stack:
            n = stack.pop()
            ans.append(n.val)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)
        return ans
        