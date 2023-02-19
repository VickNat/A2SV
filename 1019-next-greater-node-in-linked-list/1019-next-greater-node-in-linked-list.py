# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        dummy = ListNode(0)
        dummy.next = head
        stack = []
        size = 0
        ptr = 0
        
        while head:
            size += 1
            head = head.next

        head = dummy.next
        ans = [0]*size
        
        while head:
            val = head.val
            
            if len(stack) == 0:
                stack.append(val)
                head = head.next
            elif stack[-1] < val:
                temp = ptr - 1
                
                while len(stack) > 0 and stack[-1] < val:
                    if ans[temp] == 0:
                        ans[temp] = val
                        stack.pop()
                    temp -= 1
                
                stack.append(val)
                head = head.next
                    
            elif stack[-1] >= val:
                stack.append(val)
                head = head.next
            
            ptr += 1

        return ans
                
                
                
                
                
                
                
                
     