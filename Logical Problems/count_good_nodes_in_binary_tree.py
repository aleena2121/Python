class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    """
    This function return the number of good nodes in the binary tree.
    
    Args: 
    root: root node of the tree
    
    Returns:
    Number of good nodes
    """
    def dfs(root, max_so_far):
        if not root:
            return 0
        good = 1 if root.val >= max_so_far else 0
        max_so_far = max(max_so_far, root.val)
        left = dfs(root.left, max_so_far)
        right = dfs(root.right, max_so_far)
        return good + left + right
    
    return dfs(root, root.val)

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

print(goodNodes(root))

