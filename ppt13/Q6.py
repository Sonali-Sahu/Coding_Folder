# Given two sorted linked lists consisting of **N** and **M** nodes respectively. 
# The task is to merge both of the lists (in place) and return the head of the merged list.

# **Examples:**

# Input: a: 5->10->15, b: 2->3->20

# Output: 2->3->5->10->15->20

# Input: a: 1->1, b: 2->4

# Output: 1->1->2->4


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

def mergeLists(headA, headB):
 
    # A dummy node to store the result
    dummyNode = Node()
 
    # Tail stores the last node
    tail = dummyNode
    while True:
 
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break
 
        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next
 
        # Advance the tail
        tail = tail.next
 
    # Returns the head of the merged list
    return dummyNode.next

# create a link list

head = newNode(5)
head.next = newNode(7)
head.next.next = newNode(15)
head.next.next.next = newNode(17)
head.next.next.next.next = newNode(19)
head.next.next.next.next.next = newNode(21)

head2 = newNode(1)
head2.next = newNode(2)
head2.next.next = newNode(3)
head2.next.next.next = newNode(4)
head2.next.next.next.next = newNode(6)

mergedsortedlist = mergeLists(head, head2)
printLinkList(mergedsortedlist)

output:- 
abc@57cce4964e78:~/workspace/dsa$ python -m linklist
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 15 -> 17 -> 19 -> 21 -> NULL
