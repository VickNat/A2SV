# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        heap = []

        for node in lists:
            if node:
                heappush(heap, node)
        
        dummy = cur = ListNode(0)

        while heap:
            node = temp = heappop(heap)
            node = node.next
            temp.next = None

            cur.next = temp
            if node:
                heappush(heap, node)
            cur = cur.next
        
        return dummy.next