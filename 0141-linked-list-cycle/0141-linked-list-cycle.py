# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        answer = False
        fast = head
        slow = head
        
        while fast and slow:
            fast = fast.next
            slow = slow.next
            
            if fast and fast.next and fast.next is slow:
                answer = True
                break
            
            if fast:
                fast = fast.next
        
        return answer