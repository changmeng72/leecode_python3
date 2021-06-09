# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head==None:
            return 0
            
        r = head.val
        head = head.next
        while head!=None:
            r = r<<1
            r += head.val
            head = head.next
        return r
            