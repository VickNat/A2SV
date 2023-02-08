# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            pNode = None
            curNode = head
            nNode = None
            
            while curNode:
                nNode = curNode.next
                
                if nNode:
                    if curNode.val != nNode.val:
                        pNode = curNode
                        curNode = nNode
                        nNode = curNode.next
                        
                    elif curNode.val == nNode.val:
                        while nNode is not None and nNode.val == curNode.val:
                            nNode = nNode.next
                        
                        if curNode == head:
                            curNode = nNode
                            head = curNode
                        else:
                            curNode = nNode
                        
                        if curNode:
                            nNode = curNode.next
                            
                        if pNode:
                            pNode.next = curNode
                else:
                    if pNode:
                        pNode.next = curNode
                        
                    curNode = curNode.next
                
        return head
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
        