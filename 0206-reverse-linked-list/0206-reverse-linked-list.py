# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pNode = None
        curNode = head
        nNode = None
        
        while curNode:
            nNode = curNode.next
            curNode.next = pNode
            pNode = curNode
            curNode = nNode
                    
        return pNode
        

                