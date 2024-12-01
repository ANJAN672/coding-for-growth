"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return None
        old_to_new={}
        curr=head
        while curr:
            old_to_new[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            new_node=old_to_new[curr]
            new_node.next=old_to_new[curr.next] if curr.next else None
            new_node.random=old_to_new[curr.random] if curr.random else None
            curr=curr.next
        return old_to_new[head]