class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):
    """
    This function traverses the linked list and prints the values
    """
    while head != None:
        print(f"{head.data} -> ",end="")
        head = head.next
    print("None")

head = Node(10)
head.next =  Node(20)
head.next.next = Node(30)
traverse(head)