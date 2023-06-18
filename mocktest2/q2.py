# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = ListNode(0)
        n1 = n2 = ""
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next

        res = str(int(n1[::-1])+int(n2[::-1]))[::-1]
        for i in res:
            p1.next = ListNode(i)
            p1 = p1.next
        return p2.next
        
