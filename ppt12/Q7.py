# Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
# For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, 
# the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. 





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


def merge(p, q):
    p_curr = p
    q_curr = q

    while p_curr != None and q_curr != None:      
        p_next = p_curr.next
        q_next = q_curr.next

        
        q_curr.next = p_next  
        p_curr.next = q_curr  

        p_curr = p_next
        q_curr = q_next
        q = q_curr
    return p
  
  
# create a link list

head = newNode(5)
head.next = newNode(7)
head.next.next = newNode(17)
head.next.next.next = newNode(13)
head.next.next.next.next = newNode(11)

head2 = newNode(12)
head2.next = newNode(10)
head2.next.next = newNode(2)
head2.next.next.next = newNode(4)
head2.next.next.next.next = newNode(6)

print(printLinkList(merge(head, head2)))


# Output

Printing a link list
5 -> 7 -> 17 -> 13 -> 11 -> NULL
After Del N after M Nodes None
5 -> 12 -> 7 -> 10 -> 11 -> 2 -> NULL
None
