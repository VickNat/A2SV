# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeDict = defaultdict(int)
        curNode = head
        
        while curNode:
            nodeDict[curNode] += 1
            
            if nodeDict[curNode] > 1:
                break
            
            curNode = curNode.next
        
        if curNode:
            return curNode
        else:
            return None