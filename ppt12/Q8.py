# A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle.

# Given a singly linked list, find if the linked list is circular or not. 

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
  
  
  def Circular(head):
    if head == None:
        return True
  
    # Next of head
    node = head.next
    i = 0
  
    # This loop would stop in both cases (1) If
    # Circular (2) Not circular
    while((node is not None) and (node is not head)):
        i = i + 1
        node = node.next
  
    return(node == head)
  
  
# create a link list

head = newNode(5)
head.next = newNode(7)
head.next.next = newNode(17)
head.next.next.next = newNode(13)
head.next.next.next.next = newNode(11)
head.next.next.next.next.next = head


print("The LinkList is Circular os not:- True/False = ",Circular(head))


# Output:- 
abc@2389486b1a5f:~/workspace/dsa$ python -m linklist
The LinkList is Circular os not:- True/False =  True
