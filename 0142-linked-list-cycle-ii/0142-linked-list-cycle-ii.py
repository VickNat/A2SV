# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPtr = head
        slowPtr = head
        meetPtr = head
        
        while fastPtr and fastPtr.next and slowPtr:
            
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            
            if fastPtr == slowPtr:
                break
        
        while meetPtr and fastPtr:
            if meetPtr == fastPtr:
                break
            
            fastPtr = fastPtr.next
            meetPtr = meetPtr.next
        
        if fastPtr and meetPtr == fastPtr and fastPtr.next:
            return meetPtr
        
        return None