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

def insert_at_beginning(head,value):
    """
    This function inserts a node with the given value at the beginning of the linked list
    """
    new_node = Node(value)
    new_node.next = head
    head.prev = new_node
    return new_node
    
def insert_at_end(head,value):
    """
    This function inserts a node with the given value at the end of the linked list
    """
    new_node = Node(value)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head

def insert_at_middle(head, position, value):
    """
    This function inserts a node with the given value at the given position in the linked list
    """
    if position == 1:
        return insert_at_beginning(head,value)

    new_node = Node(value)
    curr = head
    count = 1

    while curr.next is not None and count < position - 1:
        curr = curr.next
        count += 1
    new_node.next = curr.next
    curr.next = new_node
    new_node.prev = curr
    if new_node.next is not None:
        new_node.next.prev = new_node

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

print("Insertion at beginning - ")
head = insert_at_beginning(head,5)
print_linked_list(head)

print("Insertion at end - ")
head = insert_at_end(head,60)
print_linked_list(head)

print("Insertion at middle - ")
head = insert_at_middle(head,4,25)
print_linked_list(head)