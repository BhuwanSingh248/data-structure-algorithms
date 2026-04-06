# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        response = ListNode(0)
        carry = 0
        temp = response

        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val
                val = val + carry
                if val > 9:
                    carry = val // 10
                    val = val % 10
                else:
                    carry = 0
                temp.next = ListNode(val)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + carry
                if val > 9:
                    carry = val // 10
                    val = val % 10
                else:
                    carry = 0
                temp.next = ListNode(val)
                l1 = l1.next
            elif l2:
                val = l2.val + carry
                if val > 9:
                    carry = val // 10
                    val = val % 10
                else:
                    carry = 0
                temp.next = ListNode(val)
                l2 = l2.next
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
    
        return response.next