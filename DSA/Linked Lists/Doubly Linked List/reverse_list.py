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

def reverse(head):
    """
    This function reverses the linked list
    """
    curr = head
    temp = None

    while curr is not None:
        temp = curr.prev  # storing previos node in temp
        curr.prev = curr.next  # reversing link
        curr.next = temp
        curr = curr.prev

    return temp.prev

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

print("Reversed List - ")
head = reverse(head)
print_linked_list(head)