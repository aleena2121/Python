class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def print_linked_list(head):
    """
    This function prints the linked list in a readable format
    """
    if head is None:
        print("List is empty.")
        return

    curr = head
    while True:
        print(f"{curr.data} -> ", end="")
        curr = curr.next
        if curr == head:
            break
    print("(head)")


def insert_at_beginning(last, value):
    """
    This function inserts the given data at the beginning of the linked list
    """
    new_node = Node(value)
    if last is None:   # if linked list is empty
        new_node.next = new_node
        return new_node
    
    new_node.next = last.next
    last.next = new_node
    return last

def insert_at_end(last, value):
    """
    This function inserts the given data at the end of the linked list
    """
    new_node = Node(value)
    if last is None:   # if linked list is empty
        new_node.next = new_node
        return new_node
    
    new_node.next = last.next
    last.next = new_node
    return new_node

def insert_in_middle(last, position, value):
    """
    This function inserts a node with the given value at the given position in the linked list
    """
    if last is None:   # if linked list is empty
        if position != 1:
            print("Invalid position")
            return last
        return insert_at_beginning(last, value)
    
    if position == 1:
        return insert_at_beginning(last,value)

    new_node = Node(value)
    curr = last.next

    for i in range(1, position - 1):
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
    return last
    


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = node1  

last = node3  
head = last.next

print("Original List -")
print_linked_list(head)

print("Insertion at the beginning - ")
last = insert_at_beginning(last, 5)
print_linked_list(last.next)

print("Insertion at the end - ")
last = insert_at_end(last, 40)
print_linked_list(last.next)

print("Insertion in middle - ")
last = insert_in_middle(last,4,25)
print_linked_list(last.next)