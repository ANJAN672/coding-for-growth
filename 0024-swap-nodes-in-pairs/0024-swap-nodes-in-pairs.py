# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        while t and t.next:
            t.val, t.next.val = t.next.val, t.val
            t = t.next.next
        return head