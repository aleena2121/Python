class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def search(head,key):
    """
    This function searches the given value in the linked list
    """
    curr = head
    while curr is not None:
        if curr.data == key:
            return "Found"
        curr = curr.next
    
    return "Not Found"

head = Node(10)
head.next =  Node(20)
head.next.next = Node(30)
print(search(head,21))