# Write a function that takes a list sorted in 
# non-decreasing order and deletes any duplicate nodes from the list. 
# The list should only be traversed once.

# For example if the linked list is 11->11->11->21->43->43->60 then 
# removeDuplicates() should convert the list to 11->21->43->60.

# # link list structure
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




def removeDuplicates(ptr):
    temp = ptr

    if temp is None:
        return 
    while temp.next is not None:
        if temp.data == temp.next.data:
            new = temp.next.next
            temp.next = None
            temp.next = new
        else:
            temp = temp.next
    return temp
  
unique_list = removeDuplicates(head)
printLinkList(unique_list)
