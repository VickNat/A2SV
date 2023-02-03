# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counts = 0
        
        if head is None or head.next is None  :
            return head
        
        size = 1
        dNode = head
        
        while dNode.next is not None:
            dNode = dNode.next
            size += 1
        
        rotate = k%size
        
        while counts < rotate:
            curNode = head
            pNode = None
            hHead = head
            
            while curNode.next is not None:
                pNode = curNode
                curNode = curNode.next
            
            if pNode is not None:
                pNode.next = None
                
            curNode.next = hHead
            head = curNode
            
            counts += 1
        
        return head