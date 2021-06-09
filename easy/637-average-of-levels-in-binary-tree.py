# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = deque([root])
        res = []
        s =  root.val
        while stack:
            res.append(s/len(stack))
            s = 0
            
            for i in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    s += node.left.val
                    stack.append(node.left)
                if node.right:
                    s += node.right.val
                    stack.append(node.right)
        return res
                    
        
        """
        stack = []
        
        stack.append(root)
        res = []
        s = root.val
        while stack:
            res.append(s/len(stack))
            s = 0
            stack2 = []
            for i in range(len(stack)):
                n = stack.pop()
                if n.left:
                    stack2.append(n.left)
                    s += n.left.val
                if n.right:
                    stack2.append(n.right)
                    s += n.right.val
            stack = stack2
           
        return res
      """      
            
        