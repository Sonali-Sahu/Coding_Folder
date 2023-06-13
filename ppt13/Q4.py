# Given a linked list, write a function to reverse every 
# alternate k nodes (where k is an input to the function) in an efficient way. 
# Give the complexity of your algorithm.
# time complexity :-O(n)


# link list structure
class Node:
    def __init__(self):
        self.data = 0
        self.next = None


# utility to create linklist node
def newNode(val):
    temp = Node()
    temp.data = val
    temp.next = None
    return temp

# utility to print a linklist
def printLinkList(pointer):
    while(pointer!=None):
        print(pointer.data,"->",end=" ")
        pointer = pointer.next
    
    print("NULL")
    
def reverse(head, k):
    if head == None:
      return None
    current = head
    next = None
    prev = None
    count = 0

    while(current is not None and count < k):
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next is not None:
        head.next = self.reverse(next, k)

    return prev
 
head = newNode(5)
head.next = newNode(5)
head.next.next = newNode(17)
head.next.next.next = newNode(15)
head.next.next.next.next = newNode(11)

new_list = reverse(head,2)
printLinkList(new_list)
  
 
