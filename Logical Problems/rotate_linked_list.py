class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    """
    This function returns the hrad of the linked list after rotating it k times
    
    Args:
    head: head node of the linked list
    k: number of rotations to be done
    
    Returns:
    head of the rotated linked list
    """
    if head is None or head.next is None:
        return head

    length = 1
    curr = head
    while curr.next is not None:
        curr = curr.next
        length += 1
    k = k % length

    while k > 0:
        curr = head
        while curr.next and curr.next.next is not None:
            curr = curr.next
        last = curr
        last = curr.next
        curr.next = None
        last.next = head
        head = last
        k -= 1
    return head
        
