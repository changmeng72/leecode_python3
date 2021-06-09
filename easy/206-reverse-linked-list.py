# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head:
            head1 = None
            while head.next:            
                t = head.next;
                head.next = head1
                head1 = head
                head = t
            head.next = head1
        return head
        