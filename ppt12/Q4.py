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
def isllistPalin(pointer):
    slow = pointer
    stack = []
    ispalin = True

    while slow !=None:
        stack.append(slow.data)
        slow = slow.next

    
    while pointer != None:
        i = stack.pop()

        if pointer.data == i:
            ispalin  = True
        else:
            ispalin = False
            break

        pointer = pointer.next

    return ispalin
  
  
  
  
  
  # create a link list

head = newNode(1)
head.next = newNode(2)
head.next.next = newNode(3)
head.next.next.next = newNode(2)
head.next.next.next.next = newNode(1)


print("Printing a link list")
printLinkList(head)

# check if linklist is palin

print(isllistPalin(head))


# output
abc@904d9d66f7db:~/workspace/dsa$ python -m linklist
Printing a link list
1 -> 2 -> 3 -> 2 -> 1 -> NULL
True
abc@904d9d66f7db:~/workspace/dsa$ python -m linklist
Printing a link list
1 -> 2 -> 3 -> 2 -> 2 -> NULL
False





