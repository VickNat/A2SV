# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curNode = head
        size = 0
        
        if (head.next is None and n <= 1) or head is None:
            head = None
            return head
        
        while curNode is not None:
            curNode = curNode.next
            size += 1
        
        offset = size - (n+1)
        pNode = head
        idx = 0
        
        if offset > 0:
            while idx != offset:
                pNode = pNode.next

                idx += 1
        
            temp = pNode.next
            
            if pNode.next is not None:
                pNode.next = pNode.next.next
            
            temp.next = None

            return head
        
        if size == n:
            head = head.next
        else:
            head.next = head.next.next
            
        return head
            