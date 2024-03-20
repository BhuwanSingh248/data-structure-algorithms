# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp = list1
        count = 0
        x = None
        while(list1):
            count += 1
            
            if count == a:
                x= list1.next
                list1.next = list2
                while (list1.next):
                    list1 = list1.next
                
                for i in range(a,b):
                    x = x.next
                list1.next = x.next
            list1 = list1.next
        # print(x)
        return temp            
            

                