#Given a linked list and a key to be deleted.
# Delete last occurrence of key from linked. The list may have duplicates.


def deleteLast(head, x):
  
    temp = head
    ptr = None
      
    while (temp != None): 
          
        # If found key, update
        if (temp.data == x):
            ptr = temp     
              
        temp = temp.next
      
    # If the last occurrence is the last node
    if (ptr != None and ptr.next == None): 
        temp = head
        while (temp.next != ptr):
            temp = temp.next
              
        temp.next = None
      
    # If it is not the last node
    if (ptr != None and ptr.next != None): 
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
          
    return head

# create a link list

head = newNode(5)
head.next = newNode(5)
head.next.next = newNode(17)
head.next.next.next = newNode(15)
head.next.next.next.next = newNode(11)

# added in 2nd attempt
head.next.next.next.next.next = newNode(5)


unique_list = deleteLast(head, 5)
printLinkList(unique_list)

output:-
abc@57cce4964e78:~/workspace/dsa$ python -m linklist
5 -> 17 -> 15 -> 11 -> NULL
abc@57cce4964e78:~/workspace/dsa$ python -m linklist
5 -> 5 -> 17 -> 15 -> 11 -> NULL




