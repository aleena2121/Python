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

def reverse(head):
    """
    This function reverses the linked list given
    """
    prev = None  # this pointer will store the reversed linked list, initially None
    curr = head  # keeps track of the current node in list

    while curr is not None:
        next = curr.next  # stores next node
        curr.next = prev  # reverses nodes
        prev = curr 
        curr = next
    return prev

head = Node(10)
head.next =  Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original Linked List -")
print_linked_list(head)

head = reverse(head)
print("Reversed Linked List -")
print_linked_list(head)