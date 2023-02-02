# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curVal = head
        revList = []
        
        if curVal is None or curVal.next is None:
            return curVal
        
        while curVal.next is not None:
            revList.append(curVal.val)
            curVal = curVal.next
        
        revList.append(curVal.val)
        
        print(revList)
                
        right = len(revList) - 1
        
        head = None
        
        while right >= 0:
            addIdx = ListNode(revList[right], None)
            
            if head is None:
                head = addIdx
                # head = head.next
                # print(head.val)
            else:
                curVal = head
                # print(2)
                while curVal.next is not None:
                    curVal = curVal.next
                    
                
                curVal.next = addIdx
                # print(curVal.val)
                
            right -= 1
        
        return head
                