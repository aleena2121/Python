class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node):
    """
    This function performs inorder traversal of the tree
    """
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data,end=" ")
    inorder_traversal(node.right)

def insert(root, value):
    """
    This function inserts the given value in the bst
    """
    new_node = Node(value)

    if root is None:
        root = new_node
        return root
    
    if root.data == value:
        return root
    if root.data < value:
        root.right = insert(root.right, value)
    elif root.data > value:
        root.left = insert(root.left, value)
    return root


root = Node(5)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(9)

print("Original Tree : ")
inorder_traversal(root)

root = insert(root, 4)

print("\nAfter Insertion : ")
inorder_traversal(root)
