class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values if nodes exist, else 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = v1 + v2 + carry
            carry = total // 10
            
            # Create new node and move pointer
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Advance input lists if possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next