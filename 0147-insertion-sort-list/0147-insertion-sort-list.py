# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cmpNode = head
        insNode = head.next
        prevInsNode = head
        
        while insNode:
            nNode = insNode.next
            pNode = dummy
            
            while cmpNode != insNode and insNode.val > cmpNode.val:
                cmpNode = cmpNode.next
                pNode = pNode.next
            
            if cmpNode != insNode:
                pNode.next = insNode
                insNode.next = cmpNode
                prevInsNode.next = nNode  
            else:
                prevInsNode = prevInsNode.next
                
            insNode = nNode
            cmpNode = dummy.next
        
        return dummy.next
            
                
                
            