class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    """
    This function returns if there is any cycle in the linked list

    Args:
    head: head node of the linked list

    Returns:
    True if there is a cycle, False otherwise
    """
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False



head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next = head.next

print(hasCycle(head))