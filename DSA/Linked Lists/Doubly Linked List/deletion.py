class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def print_linked_list(head):
    """
    This function prints the linked list in a readable format
    """
    while head is not None:
        print(f"{head.data} -> ",end="")
        head = head.next
    print("None")

def delete_from_beginning(head):
    """
    This function delete the node at the beginning of the linked list
    """
    if head is None: # if no nodes exist
        return None
    
    if head.next is None:
        return None
    
    head = head.next
    head.prev = None
    return head
    
def delete_from_end(head):
    """
    This function delete the node at the end of the linked list
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

def delete_from_middle(head, position):
    """
    This function deletes the node at the given position in the linked list
    """
    if head is None: # if no nodes exist
        return None
    
    if position == 1:
        return delete_from_beginning(head)

    curr = head
    count = 1
    while curr is not None and count < position - 1:
        curr = curr.next
        count += 1
    if curr is None or curr.next is None:
        return None

    curr.next.next.prev = curr
    curr.next = curr.next.next
    return head

head = Node(10)
second =  Node(20)
third = Node(30)
fourth = Node(40)
fifth = Node(50)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

print("Original List -")
print_linked_list(head)

print("Deletion from beginning - ")
head = delete_from_beginning(head)
print_linked_list(head)

print("Deletion from end - ")
head = delete_from_end(head)
print_linked_list(head)

print("Deletion from middle - ")
head = delete_from_middle(head,2)
print_linked_list(head)