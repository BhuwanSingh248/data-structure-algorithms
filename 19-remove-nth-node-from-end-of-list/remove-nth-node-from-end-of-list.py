# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = head
        for _ in range(n):
            temp = temp.next

        while temp and temp.next:
            curr = curr.next
            temp = temp.next
        
        if temp == None:
            if curr.next == None:
                return None
            else:
                return curr.next

        if curr and curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        print(temp, curr)
        return head
        

            