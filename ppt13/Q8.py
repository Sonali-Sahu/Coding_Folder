# Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

# **Example 1:**

# ```
# Input:
# LinkedList = 1 <--> 3 <--> 4
# x = 3
# Output:1 3
# Explanation:After deleting the node at
# position 3 (position starts from 1),
# the linked list will be now as 1->3.






# Python implementation to delete
# a doubly Linked List node
# at the given position

# A node of the doubly linked list
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

# Function to delete a node in a Doubly Linked List.
# head_ref -. pointer to head node pointer.
# del -. pointer to node to be deleted.
def deleteNode(head_ref, del_):

	# base case
	if (head_ref == None or del_ == None):
		return

	# If node to be deleted is head node
	if (head_ref == del_):
		head_ref = del_.next

	# Change next only if node to be deleted is NOT
	# the last node
	if (del_.next != None):
		del_.next.prev = del_.prev

	# Change prev only if node to be deleted is NOT
	# the first node
	if (del_.prev != None):
		del_.prev.next = del_.next
		
	return head_ref

# Function to delete the node at the given position
# in the doubly linked list
def deleteNodeAtGivenPos(head_ref,n):

	# if list in None or invalid position is given
	if (head_ref == None or n <= 0):
		return

	current = head_ref
	i = 1

	# traverse up to the node at position 'n' from
	# the beginning
	while ( current != None and i < n ):
		current = current.next
		i = i + 1

	# if 'n' is greater than the number of nodes
	# in the doubly linked list
	if (current == None):
		return

	# delete the node pointed to by 'current'
	deleteNode(head_ref, current)
	
	return head_ref

# Function to insert a node at the beginning
# of the Doubly Linked List
def push(head_ref, new_data):

	# allocate node
	new_node = Node(0)

	# put in the data
	new_node.data = new_data

	# since we are adding at the beginning,
	#prev is always None
	new_node.prev = None

	# link the old list of the new node
	new_node.next = (head_ref)

	# change prev of head node to new node
	if ((head_ref) != None):
		(head_ref).prev = new_node

	# move the head to point to the new node
	(head_ref) = new_node
	
	return head_ref

# Function to print nodes in a given doubly
# linked list
def printList(head):

	while (head != None) :
		print( head.data ,end= " ")
		head = head.next
	
# Driver program to test above functions

# Start with the empty list
head = None

# Create the doubly linked list 10<.8<.4<.2<.5
head = push(head, 5)
head = push(head, 2)
head = push(head, 4)
head = push(head, 8)
head = push(head, 10)

print("Doubly linked list before deletion:")
printList(head)

n = 2

# delete node at the given position 'n'
head = deleteNodeAtGivenPos(head, n)

print("\nDoubly linked list after deletion:")

printList(head)

# This code is contributed by Arnab Kundu
