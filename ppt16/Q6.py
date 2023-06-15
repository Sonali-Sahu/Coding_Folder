# Given an integer k and a queue of integers, The task is to reverse the order of the
# first k elements of the queue, leaving the other elements in the same relative order.


from collections import deque

def reverse_first_k(q, k):
	solve(q, k)
	s = len(q) - k
	for _ in range(s):
		x = q.popleft()
		q.append(x)
	return q

def solve(q, k):
	if k == 0:
		return
	e = q.popleft()
	solve(q, k - 1)
	q.append(e)

# Driver code
queue = deque([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
k = 5
queue = reverse_first_k(queue, k)

# Printing queue
while queue:
	print(queue.popleft(), end=' ')
