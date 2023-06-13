# You are given the `head` of a linked list with `n` nodes.

# For each node in the list, find the value of the **next greater node**. That is, for each node,
# find the value of the first node that is next to it and has a **strictly larger** value than it.

# Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith`
# node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # initializing the position
		pos = -1
        stack = []
        
        # List[int] to be returned
		ans = []
        
		#traverse the linked list till you reach the end of it
		while head:
			# increment the pos
            pos += 1

			# appending a zero when we start with the head
			ans.append(0)

			# If the stack has some value and the top of stack has value less than the current linked list node value,
			# pop the stack and insert the value of current node at that index
			# do that till the stack is empty. This means for all the values on the left, current value is the next greater
			while stack and stack[-1][1] < head.val:
                idx, _ = stack.pop()
                ans[idx] = head.val
            
			# push the (index, head.val on the stack to compare with on the next iteration)
			stack.append((pos, head.val))
            head = head.next
        return ans
