# Given a linked list of size N. The task is to reverse every k nodes 
# (where k is an input to the function) in the linked list. If the number 
# of nodes is not a multiple of k then left-out nodes, in the end, should be 
# considered as a group and must be reversed (See Example 2 for clarification).

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


def reverse( head, k):
 
    if (head == None):
        return head

    q = []
 
    current = head
    i = 0
    while (current != None) :
        i = 1
        while (i <= k) :
            if (current == None):
                break
            q.append(current)
            current = current.next
            i = i + 1
         
        while (len(q) > 0):
            front = q[-1]
            last = q[0]
             
            temp = front.data
            front.data = last.data
            last.data = temp
 
            if (len(q) > 0):
                q.pop()

            if (len(q)):
                q.pop(0)
     
    return head
 
head = newNode(5)
head.next = newNode(5)
head.next.next = newNode(17)
head.next.next.next = newNode(15)
head.next.next.next.next = newNode(11) 


new_linklist = reverse(head,2)
 
