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
    This functio reverses the linked list given
    """
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
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