# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        left=None
        n=0 
        def transverse(right, cnt):
            nonlocal n, left
            if not right: return
            n=max(n, cnt+1)
            transverse(right.next, cnt+1)

            if cnt<=n//2: return

            Next=left.next
            left.next=right
            right.next=Next
            left=Next

        if not head or not head.next or not head.next.next: return
        left=head
        transverse(head.next, 2)
        left.next=None 
        