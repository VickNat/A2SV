# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        curNode = head
        fastNode = head.next
        delNode = None
        
        while curNode is not None:
            
            if fastNode is not None and curNode.val == fastNode.val:
                delNode = fastNode
                fastNode = fastNode.next
            elif fastNode is not None and curNode.val != fastNode.val:
                if delNode is not None:
                    delNode.next = None
                    curNode.next = fastNode
                    curNode = fastNode
                    fastNode = fastNode.next
                elif delNode is None:
                    curNode = fastNode
                    fastNode = fastNode.next
            else:
                curNode.next = None
                curNode = curNode.next
        
        return head