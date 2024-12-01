# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        f=s=d
        for _ in range(n+1):
            f=f.next
        while f is not None:
            f=f.next
            s=s.next
        s.next=s.next.next
        return d.next
