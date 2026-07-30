# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
l1 = [1,2]
l2 = [3,4]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = (nums1 + nums2)
        n = len(merged)
        
        if n % 2 == 1:
            return merged[n // 2]
        else:
            mid1, mid2 = merged[n // 2 - 1], merged[n // 2]
            return (mid1 + mid2) / 2

s = Solution()
print(s.findMedianSortedArrays(l1,l2))