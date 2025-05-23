class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    """
    This function builds a binary tree based on the given preorder and inorder traversals
    """
    if not preorder or not inorder: 
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print(buildTree(preorder,inorder))

