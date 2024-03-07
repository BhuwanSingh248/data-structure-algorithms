# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second, flag = head, head, False
        while second:
            second = second.next
            if flag:
                first = first.next
            flag = not flag
        return first