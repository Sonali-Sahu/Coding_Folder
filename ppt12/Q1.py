# Given a singly linked list, delete middle of the linked list.
# For example, 
# if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. 
# For example, if given linked list is 1->2->3->4->5->6 
# then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL



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


# count no.of nodes of a linklist

def countNodes(p):
    count = 0
    while(p!=None):
        p = p.next
        count+=1
    return count



def deleteMid(pointer):

    # edge cases
    if pointer == None:
        return None
    
    if pointer.next == None:
        return None

    p1 = pointer

    p_len = countNodes(p1)
    print(p_len)

    mid = p_len//2

    while (mid > 1):
        mid -= 1
        pointer = pointer.next
   
    pointer.next = pointer.next.next
   
    return p1

    




# create a link list

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(6)

# print a linklist
print("Printing a link list")
printLinkList(head)
print("Printing the length of the link list")
#print(countNodes(head))
new_head = deleteMid(head)
printLinkList(new_head)

# Output:- 
# Printing a link list
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> NULL
# Printing the length of the link list
# 6
# 1 -> 2 -> 3 -> 5 -> 6 -> NULL




