
# Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

# After doing so, return the head of the final linked list.  You may return any such answer.

# (Note that in the examples below, all sequences are serializations of `ListNode` objects.)


class Solution:
    def removeZeroSumSublists(self, head):
        #
        def yielder(n):
            # yielder: Access elements of Linked List (n=head initially)
            while n:
                yield n
                n = n.next
        #
        # A: nodes found
        # S: Running Sum values (always unique, since duplicates triger cleanup)
        # d: Companion dictionary for "S" (allows quick O(1) access).
        #    Entries are d[cumulative_sum] = index 
        # t: Current Running sum
        #
        A, S = [], [] 
        d    = {0:-1} 
        t    = 0      # s: Current Sum
        for n in yielder(head):
            t += n.val
            if t in d:
                # Running Sum seen before, trigger cleanup
                for _ in range(d[t]+1,len(A)):
                    A.pop()
                    d.pop(S.pop())
                t = S[-1] if S else 0
            else:
                # Append new cumulative sum (unseen before)
                A.append(n)
                S.append(t)
                d[t] = len(A) - 1
        #
        # Fix Linked List Pointers
        A.append(None)
        for i,x in enumerate(A[:-1]):
            x.next = A[i+1]
        return A[0]
