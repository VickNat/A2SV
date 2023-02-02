# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pNode = None
        curNode = head
        nNode = None
        
        while curNode is not None:
            nNode = curNode.next
            curNode.next = pNode
            
            pNode = curNode
            curNode = nNode
                    
        return pNode
        
        
        
        
        
        
        
        
        
#         curVal = head
#         revList = []
        
#         if curVal is None or curVal.next is None:
#             return curVal
        
#         while curVal.next is not None:
#             revList.append(curVal.val)
#             curVal = curVal.next
        
#         revList.append(curVal.val)
        
#         print(revList)
                
#         right = len(revList) - 1
        
#         head = None
        
#         while right >= 0:
#             addIdx = ListNode(revList[right], None)
            
#             if head is None:
#                 head = addIdx
#             else:
#                 curVal = head
#                 while curVal.next is not None:
#                     curVal = curVal.next
                    
                
#                 curVal.next = addIdx
                
#             right -= 1
        
#         return head
                