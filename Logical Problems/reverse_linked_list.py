class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Adds new node to the linked list
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """
        Prints the linked list
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """
        Reverses the linked list in-place.
        """
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev  


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("\nOriginal List: ",end='')
ll.display()

ll.reverse()  

print("\nReversed List ",end='')
ll.display()
