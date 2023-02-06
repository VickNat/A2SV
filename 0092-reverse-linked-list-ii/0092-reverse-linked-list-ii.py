# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pNode = None
        nNode = None
        curNode = head

        idx = 1

        while idx != left:
            pNode = curNode
            curNode = curNode.next

            idx += 1

        lHead = pNode
        lTail = curNode
        
        nNode = curNode.next

        while idx < right:
                    
            curNode.next = pNode
            pNode = curNode
            curNode = nNode
            nNode = curNode.next

            idx += 1

        curNode.next = pNode

        if lHead:
            lHead.next = curNode
        else:
            head = curNode

        lTail.next = nNode
        
        return head
        
        
                
            