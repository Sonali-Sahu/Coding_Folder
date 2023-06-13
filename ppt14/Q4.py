# You are given a special linked list with N nodes where each node has a next pointer pointing to its next node.
# You are also given M random pointers, where you will be given M number of pairs denoting two nodes a and b  i.e. a->arb = b (arb is pointer to random node).


# Structure of a node of linked list
class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.arbit = None

# Function to clone the linked list
def cloneLinkedList(head):
	# Map to store the mapping of
	# old nodes with new ones
	mp = {}
	temp = head
	nhead = Node(temp.val)
	mp[temp] = nhead

	# Loop to create duplicates of nodes
	# with only next pointer
	while temp.next:
		nhead.next = Node(temp.next.val)
		temp = temp.next
		nhead = nhead.next
		mp[temp] = nhead

	temp = head

	# Loop to clone the arbit pointers
	while temp:
		mp[temp].arbit = mp[temp.arbit]
		temp = temp.next

	# Return the head of the clone
	return mp[head]

# Function to print the linked list
def printList(head):
	result = []
	while head:
		result.append(f"{head.val}({head.arbit.val})")
		head = head.next
	print(" -> ".join(result))

# Creating a linked list with random pointer
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.arbit = head.next.next
head.next.arbit = head
head.next.next.arbit = head.next.next.next.next
head.next.next.next.arbit = head.next.next
head.next.next.next.next.arbit = head.next

# Print the original list
print("The original linked list:")
printList(head)

# Function call
sol = cloneLinkedList(head)

print("The cloned linked list:")
printList(sol)
