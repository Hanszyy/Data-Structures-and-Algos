class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Extend nums1 with nums2
        nums1[m:m+n] = nums2
        
        # Sort the merged list
        nums1.sort()

