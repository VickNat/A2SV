# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        if head:
            oddPtr = head
            evenPtr = head.next
            prevPtr = head
            index = 2

            while oddPtr and evenPtr:
                if index % 2 != 0:
                    prevPtr.next = evenPtr.next
                    evenPtr.next = oddPtr.next
                    oddPtr.next = evenPtr

                    oddPtr = evenPtr
                    evenPtr = prevPtr.next
                    index += 1
                else:
                    prevPtr = evenPtr
                    evenPtr = evenPtr.next

                    index += 1

        return dummy.next