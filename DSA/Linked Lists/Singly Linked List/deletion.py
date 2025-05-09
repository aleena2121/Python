class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_linked_list(head):
    """
    This function prints the linked list in a readable format
    """
    while head != None:
        print(f"{head.data} -> ",end="")
        head = head.next
    print("None")

    
def delete_from_beginning(head):
    """
    This function deletes node at the beginning of the linked list
    """
    if head is None: # if no nodes exist
        return None

    curr = head
    head = curr.next
    return head

def deletion_from_end(head):
    """
    This function deletes node at the end of the linked list
    """
    if head is None: # if no nodes exist
        return None
    
    if head.next is None:
        return None
    
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head

def deletion_from_middle(head, position):
    """
    This function deletes the node at the given position of the linked list
    """
    if head is None or position < 1:
        return None
    
    if position == 1:
        return head.next
    
    curr = head 
    count = 1
    while curr is not None and count < position - 1:
        curr = curr.next
        count += 1

    if curr is None or curr.next is None:
        return head
    
    curr.next = curr.next.next
    return head

head = Node(10)
head.next =  Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original Linked List -")
print_linked_list(head)

head = delete_from_beginning(head)  # deleting form beginning
print("Deleting from beginning -")
print_linked_list(head)

head = deletion_from_end(head)  # deleting from end
print("Deleting from end -")
print_linked_list(head)

head = deletion_from_middle(head,2)  # deleting from 2nd position
print("Deleting from middle -")
print_linked_list(head)