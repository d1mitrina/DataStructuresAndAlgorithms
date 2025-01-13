#Binary Trees

class TreeNode():
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def preorder_traversal(root):
    if root is None: #if root is emmpty, it will come out from the fucntions
        return 
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    
preorder_traversal(root)
    
