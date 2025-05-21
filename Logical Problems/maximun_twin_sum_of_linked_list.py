class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head):
    """
    This function finds the maximum twin sum 

    Args: 
    head: head node of linked list

    Returns:
    max_sum: maximum twin sum
    """

    # finding middle node
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    # reversing second half of linked list
    mid = slow
    prev = None
    curr = mid

    while mid:
        curr = mid
        mid = mid.next
        curr.next = prev
        prev = curr
    
    # comparing values
    l1 = head
    l2 = prev
    max_sum = float("-inf")
    while l1 and l2:
        max_sum = max(max_sum,(l1.val + l2.val))
        l1 = l1.next
        l2 = l2.next
    
    return max_sum
    

node = ListNode(5)
node.next = ListNode(4)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)

print(pairSum(node))