# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        curNode = head
        check = []
        halfCounts = 0
        sizeNode = head
        
        while sizeNode is not None:
            sizeNode = sizeNode.next
            size += 1
        
        halfSize = size//2
        
        while halfCounts < halfSize:
            check.append(curNode.val)
            curNode = curNode.next
            halfCounts += 1
            
        if size % 2 != 0:
            curNode = curNode.next
        
        right = len(check) - 1
        
        while right >= 0:
            if curNode.val != check[right]:
                return False
            
            curNode = curNode.next
            right -= 1
        
        return True