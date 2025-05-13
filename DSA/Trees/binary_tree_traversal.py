class Node:
    def __init__(self,data):
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

    
def preorder_traversal(node):
    """
    This function performs preorder traversal of the tree
    """
    if node is None:
        return
    print(node.data,end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)
    
def postorder_traversal(node):
    """
    This function performs postorder traversal of the tree
    """
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data,end=" ")

def bfs_traversal(root):
    """
    This function performs bfs traversal of the tree
    """
    if root is None:
        return
    
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print("Inorder Traversal : ",end="")
inorder_traversal(root)
print(f"\nPreorder Traversal : ",end="")
preorder_traversal(root)
print(f"\nPostorder Traversal : ",end="")
postorder_traversal(root)
print(f"\nBFS Traversal : ",end="")
bfs_traversal(root)