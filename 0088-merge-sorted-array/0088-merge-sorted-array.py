class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = m-1
        ptr2 = n-1
        
        if ptr1==-1:
            nums1.clear()
            nums1.extend(nums2)
        
        while ptr2>=0:
            if nums2[ptr2]>=nums1[ptr1]:
                
                nums1.insert((ptr1+1), nums2[ptr2])
                ptr2-=1
                nums1.pop()
            elif ptr1 == 0:
                
                nums1.insert((ptr1), nums2[ptr2])
                ptr2-=1
                nums1.pop()
            else:
                ptr1-=1
                
        