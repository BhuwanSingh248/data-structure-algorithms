# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp  = ListNode(0)
        temp.next = head
        px_sum, pxs_sum = 0, {0:temp}
        i = head
        while i:
            px_sum += i.val
            if px_sum in pxs_sum:
                delete = pxs_sum[px_sum].next
                temp_sum = px_sum + delete.val
                while delete != i:
                    del pxs_sum[temp_sum]
                    delete = delete.next
                    temp_sum += delete.val
                pxs_sum[px_sum].next = i.next
            else:
                pxs_sum[px_sum] = i
            i = i.next
        return temp.next