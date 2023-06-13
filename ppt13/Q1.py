# Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that
# the greater node among both linked list will be added to the new linked list.



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


def newList(p1,p2):
    h1 = p1 
    h2 = p2

    h = None

    while p1 != None:
        temp = Node()
        temp.next = None

        if (p1.data < p2.data):
            temp.data = p2.data
        else:
            temp.data = p1.data

        if h == None:
            h = temp
        else:
            p = h
            while(p.next != None):
                p = p.next

            p.next = temp

        p1 = p1.next
        p2 = p2.next

    return h



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


newLinkList = newList(head, head2)
printLinkList(newLinkList)

# output
abc@b2ca84fb0c9b:~/workspace/dsa$ python -m linklist
12 -> 10 -> 17 -> 13 -> 11 -> NULL
