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

def insert_at_beginning(head, value):
    """
    This function inserts the given value as a node at the beginning of the linked list
    """
    new_node = Node(value)
    new_node.next = head
    return new_node

def insert_at_end(head,value):
    """
    This function inserts the given value as a node at the end of the linked list
    """
    curr = head
    new_node = Node(value)
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node
    return head

def insert_at_middle(head, position, value):
    """
    This function inserts the given value as a node at the given position of the linked list
    """
    new_node = Node(value)
    if position == 1:
        new_node.next = head
        return new_node
    
    curr = head 
    count = 1
    while curr is not None and count < position - 1:
        curr = curr.next
        count += 1
    new_node.next = curr.next.next
    curr.next = new_node
    return head

head = Node(10)
head.next =  Node(20)
head.next.next = Node(30)

print("Original Linked List -")
print_linked_list(head)

head = insert_at_beginning(head, 2)  # adding 2 to neginning
print("Inserting at beginning -")
print_linked_list(head)

head = insert_at_end(head, 40)  # adding 40 to end
print("Inserting at end -")
print_linked_list(head)

head = insert_at_middle(head,3, 15)  # adding 15 at 3rd position
print("Inserting at middle -")
print_linked_list(head)