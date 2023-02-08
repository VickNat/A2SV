# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        pNode = dummy
        
        while head and head.next:
            if head and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                head = head.next
                pNode.next = head

            else:
                pNode = pNode.next
                head = head.next
            
        return dummy.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if head:
#             pNode = None
#             curNode = head
#             nNode = None
            
#             while curNode:
#                 nNode = curNode.next
                
#                 if nNode:
#                     if curNode.val != nNode.val:
#                         pNode = curNode
#                         curNode = nNode
#                         nNode = curNode.next
                        
#                     elif curNode.val == nNode.val:
#                         while nNode is not None and nNode.val == curNode.val:
#                             nNode = nNode.next
                        
#                         if curNode == head:
#                             curNode = nNode
#                             head = curNode
#                         else:
#                             curNode = nNode
                        
#                         if curNode:
#                             nNode = curNode.next
                            
#                         if pNode:
#                             pNode.next = curNode
#                 else:
#                     if pNode:
#                         pNode.next = curNode
                    
#                     curNode = curNode.next
                
#         return head
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
        