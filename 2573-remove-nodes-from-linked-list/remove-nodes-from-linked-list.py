# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        stack = []
        while start:
            while stack and stack[-1].val < start.val:
                stack.pop()
            stack.append(start)
            start = start.next
        
        nxt = None
        while stack:
            start = stack.pop()
            start.next = nxt
            nxt = start
        return start

            
