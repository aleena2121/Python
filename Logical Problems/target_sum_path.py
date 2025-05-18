class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 

def dfs(root, path, result, target_sum):
        if root is None:
            return
        path.append(root.data)
        if sum(path) == target_sum:
            result.append(path[:])
        if root.left is not None:
            dfs(root.left, path, result, target_sum)
        if root.right is not None:
            dfs(root.right, path, result, target_sum)
        path.pop()
        return result
    

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

result = []
print(dfs(root,[],result,22))
