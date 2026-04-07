# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return True

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_half_ll = self.reverseList(slow.next)
        start = head
        while second_half_ll:
            if start.val != second_half_ll.val:
                return False

            start = start.next
            second_half_ll = second_half_ll.next
        return True

    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        return prev