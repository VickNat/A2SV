# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, curNode, pNode):
        if not curNode:
            return pNode
        
        nNode = curNode.next
        curNode.next = pNode
        
        return self.reverse(nNode, curNode)
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pNode = None
        
        return self.reverse(head, pNode)
        

                