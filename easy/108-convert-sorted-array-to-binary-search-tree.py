# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l = len(nums)
        m = l//2
        n = TreeNode(nums[m])
        if m>0:
            n.left = self.sortedArrayToBST(nums[:m])
        if m<l-1:
            n.right = self.sortedArrayToBST(nums[m+1:])
        return n
        