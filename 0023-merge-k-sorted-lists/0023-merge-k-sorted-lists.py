import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for l in lists:
            curr=l
            while curr is not None:
                heapq.heappush(heap,curr.val)
                curr=curr.next
        dummy=ListNode(0)
        currr=dummy
        while heap:
            val=heapq.heappop(heap)
            currr.next=ListNode(val)
            currr=currr.next
        return dummy.next