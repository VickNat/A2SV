# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = 0
        temp = head
        curNode = head
        twinSum = 0
        
        while temp:
            temp = temp.next
            size += 1
        
        half = (size/2)
        twinNode = head
        h = 0
        
        while h < half-1:
            twinNode = twinNode.next
            h += 1
        
        tNode = twinNode
        twinNode = twinNode.next
        tNode.next = None
        
        pNode = twinNode
        cNode = twinNode.next
        pNode.next = None
        
        while cNode:
            nNode = cNode.next
            cNode.next = pNode
            pNode = cNode
            cNode = nNode
        
        twinNode = pNode
        
        # print(twinNode)
        
        while curNode:
            sums = curNode.val + twinNode.val
            twinSum = max(twinSum, sums)
            
            curNode = curNode.next
            twinNode = twinNode.next
        
        return twinSum
        
                    