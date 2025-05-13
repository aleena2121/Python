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

def delete_from_beginning(last):
    """
    This function deletes the first node in the given linked list
    """
    if last is None:
        print("No node to delete")
        return last

    head = last.next
    if head == last:
        return None

    last.next = head.next
    return last

def delete_from_end(last):
    """
    This function deletes the node at the end in the given linked list
    """
    if last is None:
        print("No node to delete")
        return last
    
    if last.next == last: 
        return None
    
    curr = last
    while curr.next != last:
        curr = curr.next
    curr.next = last.next
    last = curr
    return last

def delete_from_middle(last,position):
    """
    This function deletes the node at the given position
    """
    if last is None:
        print("No node to delete")
        return last
    
    if position == 1:
        return delete_from_beginning(last)

    curr = head
    for _ in range(0, position - 1):
        curr = curr.next
        if curr == head:
            print("Invalid Position")
            return last
        
    target = curr.next
    curr.next = target.next

    if target == last:  # if target node is last node, update last
        last = curr
    return last

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

print("Original List -")
print_linked_list(head)

print("Delete from the beginning - ")
last = delete_from_beginning(last)
print_linked_list(last.next)

print("Delete from the end - ")
last = delete_from_end(last)
print_linked_list(last.next)

print("Delete from the middle - ")
last = delete_from_middle(last,3)
print_linked_list(last.next)