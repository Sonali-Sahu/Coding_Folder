# Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

# The **first** node is considered **odd**, and the **second** node is **even**, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = head
        dummy_even = head.next
        even_head = head.next

        while odd_head and even_head and odd_head.next and even_head.next:
            odd_head.next, even_head.next = odd_head.next.next, even_head.next.next
            odd_head = odd_head.next
            even_head = even_head.next

        # set even linked list at the end of odd linked list
        odd_head.next = dummy_even
        return head
