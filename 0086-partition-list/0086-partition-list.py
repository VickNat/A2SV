# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head:
            curNode = head

            while curNode is not None and curNode.val < x:
                curNode = curNode.next

            pNode = curNode
            
            if curNode:
                curNode = curNode.next
                
            nNode = None

            while curNode:
                nNode = curNode.next

                if x > curNode.val:
                    tPNode = None
                    tCurNode = head
                    temp = curNode

                    curNode = nNode

                    if curNode:
                        nNode = curNode.next

                    pNode.next = curNode

                    while tCurNode.val < x:
                        tPNode = tCurNode
                        tCurNode = tCurNode.next

                    if tPNode:
                        tPNode.next = temp
                        temp.next = tCurNode
                    else:
                        temp.next = tCurNode
                        head = temp

                else:
                    pNode = curNode
                    curNode = nNode

                    if curNode:
                        nNode = curNode.next
            
        return head
                
                
                