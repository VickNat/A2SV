# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        dummy = ListNode(0)
        dummy.next = list1
        pNode = None
        
        while list1 and list2:
            
            if list1.val == list2.val:
                temp = list2
                list2 = list2.next
                temp.next = list1.next
                list1.next = temp
                pNode = list1
                list1 = list1.next
            elif list1.val < list2.val:
                while list1.next and list1.next.val <= list2.val:
                    list1 = list1.next
                    
                temp = list2
                list2 = list2.next
                temp.next = list1.next
                list1.next = temp
                pNode = list1
                list1 = list1.next
                
            else:
                temp = list2
                list2 = list2.next
                
                if pNode:
                    temp.next = pNode.next
                    pNode.next = temp
                    pNode = pNode.next
                else:
                    temp.next = dummy.next
                    dummy.next = temp
                    list1 = temp
            
        return dummy.next
            
        
        
                    
                    
                    
                    
                    