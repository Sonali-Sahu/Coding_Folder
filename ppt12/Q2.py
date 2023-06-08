# Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.


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

    
def detectLoop(pointer):
    temp = ""

    while(pointer!=None):
        if(pointer.next == None):
            return False

        if(pointer.next == temp):
            return True

        next = pointer.next
        pointer.next = temp
        pointer = next



    return False



# create a link list

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(4)
head.next.next.next.next = newNode(5)
head.next.next.next.next.next = newNode(6)

# creating a loop in a link list
head.next.next.next.next.next = head.next.next
print(detectLoop(head))
