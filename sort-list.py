# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, root1, root2):
        dummy = ListNode()
        head = dummy

        while root1 and root2:
            if root1.val <= root2.val:
                dummy.next = root1
                root1 = root1.next
            else:
                dummy.next = root2
                root2 = root2.next
            
            dummy = dummy.next
        
        while root1:
            dummy.next = root1
            root1 = root1.next
            dummy = dummy.next
        
        while root2:
            dummy.next = root2
            root2 = root2.next
            dummy = dummy.next
        
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergeSort(root):
            if not root:
                return None
            if not root.next:
                return root

            fast = root
            slow = root

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            leftRoot = root
            rightRoot = slow.next
            slow.next = None

            root1 = mergeSort(leftRoot)
            root2 = mergeSort(rightRoot)

            return self.merge(root1, root2)
        
        return mergeSort(head)