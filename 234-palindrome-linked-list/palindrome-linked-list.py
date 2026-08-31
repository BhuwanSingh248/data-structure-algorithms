# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        current = slow
        while current :
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        start = head
        mid = prev
        while mid:
            if start.val != mid.val:
                return False
            mid = mid.next
            start = start.next
        return True