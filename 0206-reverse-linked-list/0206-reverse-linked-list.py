# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        prev=None
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        return prev