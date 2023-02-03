# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head:
#             leftNode = head
#             rightNode = leftNode.next
            
#             while rightNode:
#                 if leftNode.val == rightNode.val:
#                     rightNode = rightNode.next
#                 else:
#                     leftNode.next = rightNode
                    
#                     leftNode = rightNode
#                     rightNode = rightNode.next
                
#             leftNode.next = rightNode
        
#         return head
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if head:
            curNode = head
            fastNode = head.next
            
            while fastNode:

                if curNode.val != fastNode.val:
                    curNode.next = fastNode
                    curNode = fastNode
                    
                fastNode = fastNode.next
            
            curNode.next = fastNode

        return head