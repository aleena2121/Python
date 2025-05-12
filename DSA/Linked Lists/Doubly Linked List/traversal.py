class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def forward_traversal(head):
    """
    This function performs forward traversal of the doubly linked list
    """
    while head is not None:
        print(f"{head.data} -> ",end="")
        head = head.next
    print("None")

def backward_traversal(tail):
    """
    This function performs backward traversal of the doubly linked list
    """
    while tail is not None:
        print(f"{tail.data} -> ", end="")
        tail = tail.prev
    print("None")
    
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

print("Forward Traversal -")
forward_traversal(head)

print("Backward Traversal -")
backward_traversal(fifth)