class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search(last,target):
    """
    This function searches the given value in the linked list
    """

    head = last.next
    curr = head

    while True:
        if curr.data == target:
            print("Target Found")
            return
        curr = curr.next
        if curr == head:
            break
    print("Target not Found")

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node6 = Node(60)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node1

last = node6
head = last.next

search(last,30)