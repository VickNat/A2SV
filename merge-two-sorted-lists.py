# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()

        def merge(list1, list2):
            nonlocal dummy
            if not list1 and not list2:
                return
            if not list1:
                dummy.next = list2
                return
            if not list2:
                dummy.next = list1
                return
            
            temp = None

            if list1.val > list2.val:
                temp = list2
                list2 = list2.next
            else:
                temp = list1
                list1 = list1.next

            temp.next = None
            dummy.next = temp
            dummy = dummy.next

            merge(list1, list2)
        
        merge(list1, list2)
        return head.next