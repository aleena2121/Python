class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs_traversal(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def insert(root, value):
    new_node = Node(value)

    if root is None:
        root = new_node
        return root
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left is None:
            node.left = new_node
            return root
        else:
            queue.append(node.left)
        if node.right is None:
            node.right = new_node
            return root
        else:
            queue.append(node.right)
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("BFS Traversal of Original Tree : ")
bfs_traversal(root)
print("\nBFS Traversal of tree after insertion : ")
root = insert(root,5)
bfs_traversal(root)